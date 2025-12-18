# 项目运行的入口文件
from cython_demo.analyzer import analyze_data
from cython_demo.calculator import add

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    data.append(add(10, 20))
    total, average = analyze_data(data)
    print(f"Total: {total}, Average: {average}")