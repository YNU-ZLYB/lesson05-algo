# -*- coding: utf-8 -*-
"""
Step 3 性能实验（tag O5-step3）+ 自主实践②：加入 Python 内置 sorted() 对比
任务：n = 1000/2000/4000/8000 随机整数数组，
     冒泡排序(自造) vs 合并排序(自造) vs sorted()(官方轮子)，timeit 每档跑 3 次取均值
检查点 3：n 翻倍时，冒泡耗时约 x4，合并耗时约 x2；n=8000 时合并比冒泡快一个数量级以上
"""
import timeit
import random
from merge_sort import merge_sort


def bubble_sort(nums):
    """冒泡排序：O(n^2) 的经典代表（对照组）"""
    n = len(nums)
    for i in range(n - 1):              # 共 n-1 轮
        for j in range(n - 1 - i):      # 每轮比较相邻对
            if nums[j] > nums[j + 1]:   # 前大后小 -> 交换
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def make_array(n):
    """生成 n 个随机整数"""
    return [random.randint(0, 100000) for _ in range(n)]


def main():
    random.seed(42)                     # 固定随机种子，结果可复现
    sizes = [1000, 2000, 4000, 8000]
    print(f"{'n':>6} | {'冒泡(秒)':>10} | {'合并(秒)':>10} | {'sorted(秒)':>10} | {'合并比冒泡快':>12}")
    print("-" * 62)
    prev_b = prev_m = None
    results = []
    for n in sizes:
        arr = make_array(n)
        # 注意 arr[:]：每次计时用数组副本，排序是原地操作，避免第二遍计时数据变了
        t_b = timeit.timeit(lambda: bubble_sort(arr[:]), number=3) / 3
        t_m = timeit.timeit(lambda: merge_sort(arr[:]), number=3) / 3
        t_s = timeit.timeit(lambda: sorted(arr[:]), number=3) / 3
        print(f"{n:>6} | {t_b:>10.4f} | {t_m:>10.4f} | {t_s:>10.4f} | {t_b / t_m:>10.1f} 倍")
        results.append((n, t_b, t_m, t_s))
        if prev_b is not None:
            print(f"       ^ n翻倍 -> 冒泡 x{t_b / prev_b:.1f}，合并 x{t_m / prev_m:.1f}")
        prev_b, prev_m = t_b, t_m

    # 自主实践②小结：轮子 vs 自造
    print("\n--- 轮子 vs 自造 ---")
    for n, t_b, t_m, t_s in results:
        print(f"n={n:>5}：sorted() 比自造合并排序快 {t_m / t_s:.1f} 倍（C 实现 + Timsort 优化）")


if __name__ == "__main__":
    main()
