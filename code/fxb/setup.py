from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "pi_cython.pyx",  # Cython源文件
        compiler_directives={
            "language_level": "3",  # 使用Python 3语法
            "optimize.unpack_method_calls": True,  # 启用优化
        },
    )
)
