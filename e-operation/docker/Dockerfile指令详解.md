

## 前置知识
通过`Dockerfile`文件构建镜像：
```sh
# 通用
docker build -t hx-nginx:v1 -f ./filename file .
# 默认
docker build -t hx-nginx:v1 .
```
> 如果当前路径下又Dockerfile文件则可以使用默认命令，如果Dockerfile不在当前目录，或构建文件不叫`Dockerfile`，则使用通用命令

- `-f`：指文件
- `./filename`： 指构建文件所在路径
- `.`： 表示上下文路径，这里指当前路径。会将当前路径中的文件作为上下文文件。该路径可以指定其他路径。一旦上下文指定后，后面的构建镜像的工作就是只能操作上文文件。不能对服务器其他文件进行操作。（如果上下文路径指定为其他的，那么必须指定Doclerfile文件的位置）

## FROM(基础镜像)
## RUN(执行命令)
```sh
# 形式一
RUN apt install vim
# 形式二
RUN ["apt","install","vim"]
```
## COPY(复制文件)

```dockerfile
# 形式一
COPY package.json /data/apps/
# 形式二
COPY ["package.json" "/data/apps/"]
# 参数
# 改变文件的权限和分组
COPY -chown=<user>:<group> COPY package.json /data/apps/
```
> 如果目标文件夹不存在，会自动创建。
## ADD(更高级的复制文件)
> 和`COPY`的使用相同，
## CMD(容器启动命令)
## ENTRYPOINT(入口点)
## ENV(环境变量)
## ARG(构建参数)
## VOLUME(定义匿名卷)
## EXPOSE(暴露端口)
## WORKDIR(指定工作目录)
## USER(指定当前用户)
## HEALTHCHECK(监控检查)
## ONBUILD：当其他镜像以当前镜像为基础时执行ONBUILD后面的命令。