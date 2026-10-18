# -*- coding: utf-8 -*-
"""
step2：100 档利率表月供二分，验证结果与暴力遍历一致（自主实践③）
场景：贷款 100 万、30 年（360 期）等额本息，年利率 2%~6% 共 100 档升序
月供随利率单调递增 -> 天然有序，满足二分查找前提
"""
import math

PRINCIPAL = 1_000_000     # 贷款本金：100 万
MONTHS = 360              # 30 年 = 360 期
TARGET = 5000             # 目标月供：5000 元

def monthly_payment(rate_pct):
    """等额本息月供公式：M = P·r·(1+r)^n / ((1+r)^n − 1)，r 为月利率"""
    r = rate_pct / 100 / 12
    f = (1 + r) ** MONTHS
    return PRINCIPAL * r * f / (f - 1)

def main():
    # 1. 自制 100 档利率表（升序）
    rates = [round(2.0 + i * 4.0 / 99, 4) for i in range(100)]
    # 2. 每档算月供 -> 月供数组也升序，可二分
    payments = [monthly_payment(r) for r in rates]

    # 3. 二分查找月供最接近 5000 的档
    low, high, count = 0, len(payments) - 1, 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if payments[mid] == TARGET:
            low = mid
            break
        elif payments[mid] < TARGET:
            low = mid + 1
        else:
            high = mid - 1
    # 循环结束时比较 low 和 low-1 两个邻居谁离 5000 更近
    best = min([low - 1, low], key=lambda i: abs(payments[i] - TARGET))
    print(f"二分查找：比较 {count} 次（log2(100) ≈ {math.log2(100):.1f}）")
    print(f"找到：第 {best + 1} 档，年利率 {rates[best]}%，月供 {payments[best]:.2f} 元")

    # 暴力遍历验证（O(n) 对照）
    best2 = min(range(len(payments)), key=lambda i: abs(payments[i] - TARGET))
    print(f"暴力验证：第 {best2 + 1} 档，年利率 {rates[best2]}%，月供 {payments[best2]:.2f} 元")
    print(f"两种方法结果一致：{best == best2}（二分 {count} 次 vs 暴力 100 次）")

if __name__ == "__main__":
    main()