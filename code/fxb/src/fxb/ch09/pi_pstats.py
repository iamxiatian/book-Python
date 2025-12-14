import cProfile
import pstats
from .pi import estimate_pi

def analyze_performance():
    # 创建性能分析器
    profiler = cProfile.Profile()

    # 开始性能分析
    profiler.enable()

    # 运行待分析的代码
    estimate_pi(5_000_000)

    # 结束性能分析
    profiler.disable()

    # 使用pstats处理分析结果
    stats = pstats.Stats(profiler)

    # 去除路径信息，简化输出
    stats.strip_dirs()

    # 按累计时间排序并输出
    stats.sort_stats("cumulative")
    print("=== 按累计时间排序（前10个）===")
    stats.print_stats(10)

    # 按函数内部时间排序并输出
    print("\n=== 按函数内部时间排序（前10个）===")
    stats.sort_stats("time")
    stats.print_stats(10)

    # 查看特定函数的调用者信息
    print("\n=== random()函数的调用者 ===")
    stats.print_callers("random")

    # 查看特定函数调用了哪些其他函数
    print("\n=== estimate_pi()函数调用的函数 ===")
    stats.print_callees("estimate_pi")


if __name__ == "__main__":
    analyze_performance()
