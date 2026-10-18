# -*- coding: utf-8 -*-
"""
自主实践①：给 merge_sort 加"递归深度打印"，观察 8000 元素的递归树深度
预期：深度约 13，因为 log2(8000) ≈ 12.97 —— 每次对半切，切 13 刀就到单元素
"""
import math
import random


def merge(a, b):
    """双指针合并两个有序数组"""
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


max_depth = 0  # 全局记录最深递归层数


def merge_sort(nums, depth=0):
    """带递归深度记录的合并排序（根节点记为第 0 层，每切一刀深度+1）"""
    global max_depth
    if depth > max_depth:
        max_depth = depth

    if len(nums) <= 1:                # 基准情形
        return nums

    mid = len(nums) // 2              # 分解
    left_sorted = merge_sort(nums[:mid], depth + 1)    # 解决（深度+1）
    right_sorted = merge_sort(nums[mid:], depth + 1)
    return merge(left_sorted, right_sorted)            # 合并


def main():
    n = 8000
    random.seed(42)
    arr = [random.randint(0, 100000) for _ in range(n)]
    merge_sort(arr)
    print(f"n = {n}")
    print(f"实测递归树最大深度 = {max_depth}")
    print(f"log2({n}) = {math.log2(n):.2f}，向上取整 = {math.ceil(math.log2(n))}")
    print(f"结论：深度 ≈ 13，因为每层对半切，2^13 = 8192 >= 8000，切 13 次必到单元素")


if __name__ == "__main__":
    main()
