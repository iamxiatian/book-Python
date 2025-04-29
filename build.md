
# 打包部署

## pypi-server


### 概述
`pypi-server`是一个简单的、可本地部署的Python包索引服务器。它允许用户在自己的内部网络或特定环境中搭建一个类似于PyPI（Python Package Index）的服务器，用于存储和分发自己开发的或内部使用的Python包。

#### 特点
- **本地部署**：可以在本地服务器或私有网络中部署，确保包的存储和分发在可控的环境中进行，适合企业内部或特定团队使用，提高了安全性和可管理性。
- **简单易用**：安装和配置相对简单，不需要复杂的设置过程。用户可以快速搭建起一个包索引服务器，方便地上传和下载包。
- **与PyPI兼容**：在一定程度上与PyPI的功能和接口兼容，使得用户可以使用熟悉的`pip`等工具来与本地的`pypi-server`进行交互，就像使用官方PyPI一样。例如，可以使用`pip install`命令从本地`pypi-server`安装包，也可以使用`twine upload`命令将包上传到`pypi-server`。

#### 使用场景
- **企业内部开发**：企业内部开发团队可以将内部开发的Python包上传到本地的`pypi-server`，方便团队成员共享和使用这些包，避免将内部包发布到公共的PyPI上，提高了包的安全性和可控性。
- **离线环境**：在一些没有网络连接或网络连接受限的离线环境中，`pypi-server`可以作为本地的包存储库，预先将所需的包上传到服务器，然后在离线环境中的设备上通过本地网络从`pypi-server`安装包。
- **测试和开发**：开发人员在进行本地开发和测试时，可以使用`pypi-server`来模拟PyPI环境，方便地测试包的上传、下载和安装过程，而不会影响到公共的PyPI服务器。



### 安装与运行
- **安装**：通常可以使用`pip`来安装`pypi - server`，命令如下：
```bash
pip install pypi-server
```
- **运行**：安装完成后，可以通过命令行启动`pypi - server`。例如，在终端中输入`pypi-server`并指定存储包的目录等参数，即可启动服务器。

```bash
pip install pypiserver                # Or: pypiserver[passlib,cache]
mkdir /data/xiaobai/packages                      # Copy packages into this directory.
pypi-server run -p 9020 /data/xiaobai/packages &      # Will listen to all IPs.
```
- **客户端使用**：在客户端，可以通过执行如下命令使用
```bash
# Download and install hosted packages.
pip install --extra-index-url http://localhost:9020/simple/ ...
```


### 身份验证
在使用 `pypi-server` 时，密码控制是一项重要的安全措施。不过，在某些特定场景下，比如在内部网络环境中，也可以选择禁用上传时的身份验证。但为了避免因疏忽而做出不合理的安全决策，通常建议启动身份验证功能。

要实现类似 Apache 的身份验证，你需要使用 `htpasswd` 文件来管理用户的密码。具体操作步骤如下：

#### 1. 安装 `passlib` 模块
解析 `htpasswd` 文件需要用到 `passlib` 模块，并且要求其版本在 1.6 及以上。你可以使用 `pip` 来安装该模块，命令如下：
```bash
pip install passlib
```

#### 2. 创建 `htpasswd` 文件

官方网站提供了利用htpasswd创建密码文件的方法，其中，htpasswd是一个由 Apache HTTP 服务器提供的实用工具，主要用于创建和管理用于基本认证的密码文件，在使用时需要提前安装对应的包。

考虑到读者较为熟悉Python，可以不使用htpasswd命令，而是直接利用passlib提供的创建和读取验证密码信息的方法，通过以下代码创建包含用户名`admin`和测试密码`abc123```的身份验证文件。

```python
>>> from passlib.apache import HtpasswdFile
>>> ht = HtpasswdFile("/data/xiaobai/packages/my.htpasswd", new=True)
>>> ht.set_password("admin", "abc123")
False
>>> ht.save()
```

此时在`/data/xiaobai/packages`目录下会生成一个存放有身份验证信息的文件`my.htpasswd`。

### 3. 带身份验证启动服务
```bash
pypi-server run -p 9020 /data/app/packages -P my.htpasswd &!
```

### 测试

通过浏览器访问服务器地址，假设服务器地址为`10.96.1.43`，则打开http://10.96.1.43:9020/,会出现如下提示信息，表明PyPI服务已经成功运行起来。

```plain
Welcome to pypiserver!

This is a PyPI compatible package index serving 0 packages.

To use this server with pip, run the following command:

        pip install --index-url http://10.96.1.43:9020/simple/ PACKAGE [PACKAGE2...]
      
To use this server with easy_install, run the following command:

        easy_install --index-url http://10.96.1.43:9020/simple/ PACKAGE [PACKAGE2...]
      
The complete list of all packages can be found here or via the simple index.

This instance is running version 2.3.2 of the pypiserver software.
```
