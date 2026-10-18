# -*- coding: utf-8 -*-
"""
自主实践③：用二分查找在真实利率表（自制 100 档）中找"月供最接近 5000 的利率"
场景：贷款 100 万元、30 年（360 期）等额本息，年利率 100 档升序。
     月供随利率单调递增 —— 满足二分查找的"有序"前提。
"""
import math


PRINCIPAL = 1_000_000     # 贷款本金：100 万
MONTHS = 360              # 30 年 = 360 期
TARGET_PAYMENT = 5000     # 目标月供：5000 元


def monthly_payment(annual_rate_pct):
    """等额本息月供公式：M = P * r * (1+r)^n / ((1+r)^n - 1)，r 为月利率"""
    r = annual_rate_pct / 100 / 12          # 年利率 -> 月利率
    if r == 0:
        return PRINCIPAL / MONTHS
    factor = (1 + r) ** MONTHS
    return PRINCIPAL * r * factor / (factor - 1)


def binary_search_closest(payments, target):
    """在升序数组 payments 中找最接近 target 的下标（二分查找，O(log n)）"""
    low, high = 0, len(payments) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if payments[mid] == target:
            return mid, count
        elif payments[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    # 循环结束时 target 应插入 low 位置，候选是 low 和 low-1 两个邻居
    best = low
    if best >= len(payments):
        best = len(payments) - 1
    if best > 0 and abs(payments[best - 1] - target) <= abs(payments[best] - target):
        best = best - 1
    return best, count


def main():
    # 自制 100 档真实利率表：年利率 2.00% ~ 6.00%，升序共 100 档
    rates = [round(2.0 + i * (4.0 / 99), 4) for i in range(100)]
    payments = [monthly_payment(r) for r in rates]   # 月供随利率单调递增，天然有序

    print(f"利率表 {len(rates)} 档：{rates[0]:.2f}% ~ {rates[-1]:.2f}%")
    print(f"月供范围：{payments[0]:.2f} ~ {payments[-1]:.2f} 元，目标 {TARGET_PAYMENT} 元")

    # 二分查找（O(log n)）
    idx, count = binary_search_closest(payments, TARGET_PAYMENT)
    print(f"\n二分查找：比较 {count} 次（log2(100) ≈ {math.log2(100):.1f}）")
    print(f"找到：第 {idx + 1} 档，年利率 {rates[idx]:.4f}%，月供 {payments[idx]:.2f} 元")

    # 暴力遍历验证（O(n) 对照）
    idx_check = min(range(len(payments)), key=lambda i: abs(payments[i] - TARGET_PAYMENT))
    print(f"暴力验证：第 {idx_check + 1} 档，年利率 {rates[idx_check]:.4f}%，月供 {payments[idx_check]:.2f} 元")
    print(f"两种方法结果一致：{idx == idx_check}（二分 {count} 次 vs 暴力 100 次）")


if __name__ == "__main__":
    main()
