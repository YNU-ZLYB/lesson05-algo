# -*- coding: utf-8 -*-
"""
step3：冒泡 vs 合并 vs 内置 sorted() 计时对比，验证 n 翻倍冒泡×4、合并×2（检查点3+自主实践②）
同时验证"轮子 vs 自造"：sorted()（C 实现 + Timsort）比自造合并排序快一个常数因子
"""
import timeit
import random

def merge(a, b):
    """双指针合并两个有序数组"""
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:]); result.extend(b[j:])
    return result

def merge_sort(nums):
    """合并排序（自包含，不依赖外部文件，单文件可直接运行）"""
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))

def bubble_sort(nums):
    """冒泡排序：O(n²) 的经典代表（对照组）"""
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

def make_array(n):
    """生成 n 个随机整数数组"""
    return [random.randint(0, 100000) for _ in range(n)]

def main():
    random.seed(42)
    print(f"{'n':>6} | {'冒泡(秒)':>10} | {'合并(秒)':>10} | {'sorted(秒)':>10} | {'合并比冒泡快':>12}")
    print("-" * 62)
    prev_b = prev_m = None
    results = []
    for n in [1000, 2000, 4000, 8000]:
        arr = make_array(n)
        # 注意 arr[:]：每次计时用数组副本，避免第二遍计时的数据被上一次排序改掉
        t_b = timeit.timeit(lambda: bubble_sort(arr[:]), number=3) / 3
        t_m = timeit.timeit(lambda: merge_sort(arr[:]), number=3) / 3
        t_s = timeit.timeit(lambda: sorted(arr[:]), number=3) / 3
        print(f"{n:>6} | {t_b:>10.4f} | {t_m:>10.4f} | {t_s:>10.4f} | {t_b / t_m:>10.1f} 倍")
        results.append((n, t_m, t_s))
        if prev_b is not None:
            print(f"       ^ n翻倍 -> 冒泡 x{t_b / prev_b:.1f}，合并 x{t_m / prev_m:.1f}")
        prev_b, prev_m = t_b, t_m

    # 自主实践②小结：轮子 vs 自造
    print("\n--- 轮子 vs 自造 ---")
    for n, t_m, t_s in results:
        print(f"n={n:>5}：sorted() 比自造合并排序快 {t_m / t_s:.1f} 倍")

if __name__ == "__main__":
    main()