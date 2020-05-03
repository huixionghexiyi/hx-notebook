# 概述

类似于docker中创建`images`使用`Dockerfile`一样,`kubernetes`创建`pod`也需要使用配置文件。
# 目标

- 应用`ConfigMap`生成器
- 应用该文件夹去运行一个`pod`
- 验证配置是否可用

# 应用`ConfigMap`生成器

```yml
# redis-config
maxmemory 2mb
maxmemory-policy allkeys-lru

# redis-pod.yaml 
pods/config/redis-pod.yaml 

apiVersion: v1
kind: Pod
metadata:
  name: redis
spec:
  containers:
  - name: redis
    image: redis:5.0.4
    command:
      - redis-server
      - "/redis-master/redis.conf"
    env:
    - name: MASTER
      value: "true"
    ports:
    - containerPort: 6379
    resources:
      limits:
        cpu: "0.1"
    volumeMounts:
    - mountPath: /redis-master-data
      name: data
    - mountPath: /redis-master
      name: config
  volumes:
    - name: data
      emptyDir: {}
    - name: config
      configMap:
        name: example-redis-config
        items:
        - key: redis-config
          path: redis.conf

# kustomization.yaml

configMapGenerator:
- name: example-redis-config
  files:
  - redis-config
resources:
- redis-pod.yaml

```

创建如上三个文件后，执行`kubectl apply -k .`,(其中k代表`kustomize`,指一个目录其中包含文件名为`kustomizeation.yaml`的目录)

```sh
kubectl apply -k . # 创建一个pod
kubectl get -k . # 查看当前文件夹创建pod的情况
kubectl exec -it redis bash # 进入容器中看一下
```

具体详情请参看[文章](https://www.jianshu.com/p/ffb1ceb7aba9)

