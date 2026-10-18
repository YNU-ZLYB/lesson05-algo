# -*- coding: utf-8 -*-
"""
step1：最小版合并排序，验证分治三步输出 [1,2,3,5,8,9]（检查点1）
代码中可指出：哪几行是"分解"、哪几行是"合并"
"""


def merge(a, b):
    """双指针合并两个有序数组（分治第三步：合并 Combine）"""
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:            # 取两者中较小者入结果
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])            # 左残段必有序，直接接上
    result.extend(b[j:])            # 右残段必有序，直接接上
    return result


def merge_sort(nums):
    """合并排序：分治三步的完整样板"""
    # 基准情形：长度 0 或 1 的数组天然有序，直接返回
    if len(nums) <= 1:
        return nums

    # ---- 分解（Divide）：从中间切成两半 ----
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]

    # ---- 解决（Conquer）：递归排序两个小段 ----
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # ---- 合并（Combine）：两个有序段拼成一个有序段 ----
    return merge(left_sorted, right_sorted)


def main():
    nums = [8, 3, 5, 1, 9, 2]
    print("排序前：", nums)
    print("排序后：", merge_sort(nums))


if __name__ == "__main__":
    main()
