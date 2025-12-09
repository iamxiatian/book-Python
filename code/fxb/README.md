# 非小白的Python代码

第3章到第5章的代码，单独存放在ch3、ch4和ch5的项目文件夹中，不包含在fxb本项目中。

第6章之后的代码，分别放在了src/fxb/ch06类似的package之下，供用户访问。

## 运行

```bash
# 同步库
uv sync

# 安装项目
uv pip install -e .

# 以module方式运行脚本，如运行src/ch06/singleton.py,可以如下运行：
uv run -m fxb.ch06.singleton
```
