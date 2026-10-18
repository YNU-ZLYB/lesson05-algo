# -*- coding: utf-8 -*-
"""
独立研究②：sys.setrecursionlimit 是干什么的？合并排序 10 万元素会不会撞递归上限？
实验：查看默认递归上限，实测 10 万元素合并排序的最大递归深度
"""
import sys
import math
import time
import random

# 先打印当前递归上限
print(f"Python 默认递归上限 sys.getrecursionlimit() = {sys.getrecursionlimit()}")
print("sys.setrecursionlimit(n) 的作用：修改解释器允许的最大递归深度，")
print("防止无限递归把 C 语言调用栈撑爆（栈溢出会让解释器直接崩溃）。")
print()


def merge(a, b):
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


max_depth = 0


def merge_sort(nums, depth=0):
    global max_depth
    if depth > max_depth:
        max_depth = depth
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_sorted = merge_sort(nums[:mid], depth + 1)
    right_sorted = merge_sort(nums[mid:], depth + 1)
    return merge(left_sorted, right_sorted)


def main():
    n = 100_000
    random.seed(42)
    arr = [random.randint(0, 1000000) for _ in range(n)]
    t0 = time.perf_counter()
    merge_sort(arr)
    t1 = time.perf_counter()
    print(f"n = {n:,}")
    print(f"实测最大递归深度 = {max_depth}（log2({n}) ≈ {math.log2(n):.2f}）")
    print(f"默认递归上限 = {sys.getrecursionlimit()}")
    print(f"排序耗时 {t1 - t0:.4f} 秒，正常完成，没有 RecursionError")
    print()
    print("结论：10 万元素不会撞递归上限。")
    print("因为合并排序的递归深度只有 O(log n)，n=10 万时深度仅约 17 层，")
    print("远小于默认上限 1000。递归深度按对数增长，是合并排序不怕大数据的原因之一。")
    print("（真正容易撞上限的是深度 O(n) 的递归，如对 1000+ 元素用递归实现快排的最坏情况。）")


if __name__ == "__main__":
    main()
