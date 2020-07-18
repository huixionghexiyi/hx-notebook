# WSL(Windows subsystem linux)

> https://docs.microsoft.com/zh-cn/windows/wsl/
> > WSL1 目前不支持docker，但是可以使用和windows同一个ip进行ssh连接；WSL2支持docker，但是不能和windows使用同一个ip进行ssh连接。
顾名思义就是`Windows`的`Linux`子系统，在Window中可以使用Linux，且用同一个网络，使用同一个`IP`，端口也是一一映射。

`WSL`有两个版本：`WSL1`和`WSL2`。`WSL1`不是一个完整的Linux内核，有他独特的地方，能和你的Windows进行更多的联动操作。而 `WSL2`则拥有一个完整的 `Linux`内核，其本质是部署在`hyperV`上的一个虚拟机，所以与windows的联动并不是那么多。

## WSL2

由于本人主要使用`WSL2`用于开发，所以原生的Linux内核能减少很多麻烦。

### 安装

- 执行以下命令打开WSL功能
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
- 下载WSL对应的Linux

在Windows的应用商城中搜索`Ubuntu`下载即可。

- 其他设置

```sh
# 设置默认为root启动
{user}ubuntu config --set-defualt-user root
# 安装wsl2的更新内核
 https://aka.ms/wsl2

# 查看当前wsl
wsl --list --verbose
# 更换为wsl2
 wsl --set-version Ubuntu-20.04 2
```

# Ubuntu调整

- 配置源
- 安装docker :https://www.jianshu.com/p/c27255ede45f

