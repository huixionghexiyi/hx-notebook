[官方Github](https://github.com/kubernetes/kubernetes)
[官方教程](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

# 介绍

根据官方介绍，大致可以这样理解。以前我们部署一个应用，直接部署到服务器上，会与服务器高度集成，很难分离、迁移业务，并且服务器故障会造成业务停止。而使用应用容器化会将这种高度集成的问题解决，但是不能做到高可用。所以`kubernetes`就是用来解决这种问题，将容器化的应用都部署到一个集群中。集群中的服务器的故障不会造成业务的停止。会有其他的服务器提供服务。

集群：即多个虚拟机或物理机的组成，抽象为一个单一单元。对外集群可以看成一个单一的服务器。实质上，是很多服务器组成的。

- 集群
    - Master节点
        - API Server: 整个集群对外的接口,提供给客户端调用
        - Scheduler: 调度集群内的资源
        - Controller manager: 管理控制器
        - etcd
    - Node节点: 一个集群中有多个节点
        - Pod: 代表集群中的一个进程，内部封装一个或多个紧密相关的容器。
        - Docker: 创建容器
        - kublet: 监视本节点上的Pod,包括创建、修改、监控、删除等
        - kube-proxy: 为Pod对象提供代理
        - Fluend: 负责日志收集、存储和查询
    - Service: 一组提供相同服务的`Pod`对外的访问接口。这些`Pod`可以在不同的节点中。是不同节点中提供相同服务的`pod`的集合。

# 部署集群

要先拥有一个集群，才能将业务部署到集群中。所以，先创建一个只有一台服务器的集群。安装好后,使用`kubectl`命令进行操控。和docker一样,也是客户端和服务端的操作(虽然客户端和服务端可能是在同一台服务器上)。

```sh
kubectl version # 将显示客户端和服务端的版本
kubectl cluster-info # 查看集群信息
kubectl get nodes # 查看集群节点信息
kubectl get deployments # 查看部署的应用
kubectl get pods # 查看所有的pod
kubectl decscribe pods # 查看pods的细节

```

# 部署应用

集群中的应用是放到`Pod`中的,(`Pod`可以看成是包含多个不同的容器以构成能够提供完整服务的应用)。集群中的应用只能与集群通信,外界要访问的话,需要设置代理。


```sh
# 部署一个应用
kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 # 部署一应用(通过镜像)
kubectl get deployments # 查看部署的应用 flannel
kubectl proxy # 使用默认代理
curl http://localhost:8001/version # 访问应用
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}') # 将pod的名字写为环境变量
kubectl logs $POD_NAME # 查看pod的日志
```

# 操作`pod`

前面是使用默认代理,让其能够被外网访问,现在是将其放到`service`中,用以提供统一的接口供外界访问。

将相同的`pod`放到一个`service`中,指定`type`就是指定网络访问的方式:
- ClusterIP: 默认方式,只能从集群内部访问
- NodePort: 公开节点的同一个端口,用户可以使用`<NodeIP>:<NodePort>`的方式访问服务。
- LoadBalancer: 分配一个可供外网访问的固定的IP。
- ExternalName: 使用一个`CNAME`暴露服务。(网上查一下啥是`CNAME`2020年1月2日)

```sh
# 将端口8000 暴露给外部,暴露端口时会创建一个service
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
# 查看服务，会发现多个一个type为NodePort的服务
kubectl get services
# 将服务的nodeport端口设置为环境变量
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT
# 通过外网访问服务(这里使用的是minikube创建的kuberneter,所以通过minikube可以获取到ip，也可以通过ip a 查看ip)
curl $(minikube ip):$NODE_PORT
# 查看部署情况,可以看到labels是：run=kubernetes-bootcamp
kubectl describe deployment
# 通过标签查询pods
kubectl get pods -l run=kubernetes-bootcamp
# 通过标签查询服务
kubectl get service -l run=kubernetes-bootcamp
# 将这个pod的名字写到环境变量中
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
# 将这个pod的变迁修改为 v1
kubectl label pod $POD_NAME app=v1
# 再查看标签,已经被改成了 app=v1
kubectl describe pods $POD_NAME
# 通过修改后的标签查询pod
kubectl get pods -l app=v1
# 删除服务,删除后将不能再通过外网访问
kubectl delete service -l run=kubernetes-bootcamp
# 但是可以通过内网访问,说明对外的端口已经关闭了
kubectl exec -ti $POD_NAME curl localhost:8080
```

`pod`里面是多个容器并且包括容器所依赖的`volume`、`network`,而容器里面是封装的应用。所以操作`pod`就是操作应用。

操作`pod`的方式和`docker`操作容器的方式相似。不同之处在于`docker`是对`container`操作,而`kubectl`是对`pod`进行操作。一个`pod`包含许多相同的`container`以及相关的依赖。

```bash

kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080 # 将这个pod的端口暴露出来

# docker 操作容器
docker exec -it <container> bash 
# kubernetes 操作pods
kubectl exec -it <pods-name> bash 

# docker 操作
```

# 操作`node`中的`pod`

将`pod`复制到不同的服务器上,可以保证业务总是能被访问,并且可以进行滚动升级。

```sh
kubectl get deployments # 查看当前有多少deployments
kubectl scale deployments/kubernetes-bootcamp --replicas=4 # 总共4个
kubectl get deployments # 再次查看
kubectl get pods -o wide # 查看pods的更多属性
kubectl describe deployments/kubernetes-bootcamp # 查看kubernetes-bootcamp的更多属性

###########
# 更新应用
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2 #更新刚才的应用
kubectl describe services/kubernetes-bootcamp # 查看services
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}') # 将pods的IP写入环境变量
curl $(minikube ip):$NODE_PORT # 查看应用运行结果

kubectl rollout status deployments/kubernetes-bootcamp # 确认是否更新成功

kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10 # 再更新一个不存在的镜像

kubectl get deployments # 查看会发现少了一个
kubectl get pods # 查看pods, 发现有两个pods报错
kubectl describe pods # 看详细情况,查看原因
kubectl rollout undo deployments/kubernetes-bootcamp # 回滚到之前的版本
kubectl get pods # 再次查看



```