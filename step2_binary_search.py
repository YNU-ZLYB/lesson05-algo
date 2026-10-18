# -*- coding: utf-8 -*-
"""
step2：1024 档利率表二分查找 3.75%，验证比较次数 <= 10（检查点2）
含故意实验：传入未排序数组，验证"有序前提"被破坏时结果不可预测
"""


def binary_search(rates, target):
    """在有序数组 rates 中找 target，返回下标，找不到返回 -1。
    前提：rates 必须已按升序排好——不满足此前提，结果不可预测。"""
    low, high = 0, len(rates) - 1
    count = 0                          # 记录比较次数
    while low <= high:
        count += 1
        mid = (low + high) // 2        # 看中间档
        if rates[mid] == target:
            print(f"找到 {target}，位于下标 {mid}，共比较 {count} 次")
            return mid
        elif rates[mid] < target:      # 中间偏小 -> 左半整体砍掉
            low = mid + 1
        else:                          # 中间偏大 -> 右半整体砍掉
            high = mid - 1
    print(f"没找到 {target}，共比较 {count} 次")
    return -1


def main():
    # 1024 档模拟利率表：0.01% ~ 10.24%，步长 0.01，升序
    rates = [round(0.01 * (i + 1), 2) for i in range(1024)]
    print(f"利率表共 {len(rates)} 档，范围 {rates[0]}% ~ {rates[-1]}%")

    # 检查点 2：找 3.75%
    idx = binary_search(rates, 3.75)
    print(f"验证：rates[{idx}] = {rates[idx]}，查找次数 <= 10 即达标")

    # 故意实验：传入未排序数组会怎样？
    print("\n--- 故意实验：传入未排序数组 ---")
    import random
    bad_rates = rates[:]
    random.shuffle(bad_rates)          # 打乱顺序，破坏"有序"前提
    idx2 = binary_search(bad_rates, 3.75)
    if idx2 == -1:
        print("结果：返回 -1（没找到）—— 但 3.75 明明在数组里！前提被破坏，结果不可预测。")
    else:
        print(f"结果：返回下标 {idx2}，bad_rates[{idx2}] = {bad_rates[idx2]} —— 这次'运气好'，换一组数据就可能出错。")


if __name__ == "__main__":
    main()
