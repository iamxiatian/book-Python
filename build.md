
# 打包部署

## pypi-server


### 概述
`pypi - server`是一个简单的、可本地部署的Python包索引服务器。它允许用户在自己的内部网络或特定环境中搭建一个类似于PyPI（Python Package Index）的服务器，用于存储和分发自己开发的或内部使用的Python包。

### 特点
- **本地部署**：可以在本地服务器或私有网络中部署，确保包的存储和分发在可控的环境中进行，适合企业内部或特定团队使用，提高了安全性和可管理性。
- **简单易用**：安装和配置相对简单，不需要复杂的设置过程。用户可以快速搭建起一个包索引服务器，方便地上传和下载包。
- **与PyPI兼容**：在一定程度上与PyPI的功能和接口兼容，使得用户可以使用熟悉的`pip`等工具来与本地的`pypi - server`进行交互，就像使用官方PyPI一样。例如，可以使用`pip install`命令从本地`pypi - server`安装包，也可以使用`twine upload`命令将包上传到`pypi - server`。

### 安装与运行
- **安装**：通常可以使用`pip`来安装`pypi - server`，命令如下：
```
pip install pypi-server
```
- **运行**：安装完成后，可以通过命令行启动`pypi - server`。例如，在终端中输入`pypi-server`并指定存储包的目录等参数，即可启动服务器。

```
pip install pypiserver                # Or: pypiserver[passlib,cache]
mkdir ~/packages                      # Copy packages into this directory.
pypi-server run -p 8080 ~/packages &      # Will listen to all IPs.
```
- **客户端使用**：在客户端，可以通过执行如下命令使用
```
# Download and install hosted packages.
pip install --extra-index-url http://localhost:8080/simple/ ...
```


### 使用场景
- **企业内部开发**：企业内部开发团队可以将内部开发的Python包上传到本地的`pypi - server`，方便团队成员共享和使用这些包，避免将内部包发布到公共的PyPI上，提高了包的安全性和可控性。
- **离线环境**：在一些没有网络连接或网络连接受限的离线环境中，`pypi - server`可以作为本地的包存储库，预先将所需的包上传到服务器，然后在离线环境中的设备上通过本地网络从`pypi - server`安装包。
- **测试和开发**：开发人员在进行本地开发和测试时，可以使用`pypi - server`来模拟PyPI环境，方便地测试包的上传、下载和安装过程，而不会影响到公共的PyPI服务器。
