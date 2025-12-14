import cProfile

from .pi import benchmark_pi

def main():
    benchmark_pi()

if __name__ == "__main__":
    # 创建性能分析器
    profiler = cProfile.Profile()

    # 开始性能分析
    profiler.enable()

    # 运行主函数
    main()

    # 结束性能分析
    profiler.disable()

    # 输出性能分析结果，按累计时间排序
    print("\n===== 性能分析结果（按累计时间排序） =====\n")
    profiler.print_stats(sort="cumulative")
