from pathlib import Path
from setuptools import Extension, find_packages, setup
from Cython.Build import cythonize

# 递归查找src目录下所有Python文件
py_files = list(Path("./src").rglob("*.py"))
extensions = []

# 为每个Python文件创建Cython扩展配置
for p in py_files:
    # 生成符合Python规范的模块名（如cython_demo.calculator）
    module_name = str(p.with_suffix("").relative_to("./src")).replace("/", ".")
    extensions.append(
        Extension(
            name=module_name,  # 扩展模块名称
            sources=[str(p)],  # 待编译的源文件
            language="c",  # 编译语言为C
        )
    )

# 将Python文件编译为C扩展模块
ext_modules = cythonize(extensions, annotate=False)

# 打包配置：将src下的代码编译为C扩展并构建Python包
setup(
    name="cython_demo",
    version="1.0.0",
    packages=find_packages(where="src"),  # 自动识别src下的Python包
    package_dir={"": "src"},  # 指定源码根目录为src
    ext_modules=ext_modules,  # 传入编译好的扩展模块
)
