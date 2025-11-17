#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
超级靓号生成器 - 支持前缀+后缀同时匹配
专为10位以上的超级靓号设计
"""

import os
import time
import secrets
import multiprocessing as mp
from typing import Tuple, Optional
from eth_utils import to_checksum_address
from Crypto.Hash import keccak
from eth_keys import keys


def generate_address_fast(private_key_bytes: bytes) -> Tuple[str, str]:
    """快速生成地址"""
    pk = keys.PrivateKey(private_key_bytes)
    public_key_bytes = pk.public_key.to_bytes()
    
    k = keccak.new(digest_bits=256)
    k.update(public_key_bytes)
    address_bytes = k.digest()[-20:]
    
    address = '0x' + address_bytes.hex()
    address = to_checksum_address(address)
    
    return private_key_bytes.hex(), address


def check_pattern_combined(address: str, prefix: str, suffix: str, case_sensitive: bool) -> bool:
    """
    检查前缀+后缀同时匹配
    
    Args:
        address: 地址
        prefix: 前缀（不含0x）
        suffix: 后缀
        case_sensitive: 是否区分大小写
    """
    addr = address[2:]  # 移除0x
    
    if not case_sensitive:
        addr = addr.lower()
        prefix = prefix.lower()
        suffix = suffix.lower()
    
    # 同时检查前缀和后缀
    return addr.startswith(prefix) and addr.endswith(suffix)


def worker_ultra(prefix: str, suffix: str, case_sensitive: bool,
                result_queue: mp.Queue, counter: mp.Value, stop_event: mp.Event):
    """超级靓号工作进程（优化版）"""
    local_count = 0
    
    while not stop_event.is_set():
        try:
            # 生成私钥和地址
            private_key = secrets.token_bytes(32)
            pk_hex, address = generate_address_fast(private_key)
            
            local_count += 1
            
            # 每1000次更新一次计数器（优化：更频繁的更新）
            if local_count % 1000 == 0:
                with counter.get_lock():
                    counter.value += 1000
            
            # 检查是否同时匹配前缀和后缀
            if check_pattern_combined(address, prefix, suffix, case_sensitive):
                result_queue.put((pk_hex, address, local_count))
                
        except Exception:
            continue
    
    # 更新剩余计数
    remainder = local_count % 1000
    if remainder > 0:
        with counter.get_lock():
            counter.value += remainder


def format_time(seconds: float) -> str:
    """格式化时间"""
    if seconds < 60:
        return f"{seconds:.0f}秒"
    elif seconds < 3600:
        return f"{seconds/60:.0f}分{seconds%60:.0f}秒"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return f"{hours}小时{minutes}分"
    else:
        days = int(seconds / 86400)
        hours = int((seconds % 86400) / 3600)
        return f"{days}天{hours}小时"


def format_large_number(num: int) -> str:
    """格式化大数字"""
    if num >= 1_000_000_000_000:  # 万亿
        return f"{num / 1_000_000_000_000:.2f}万亿"
    elif num >= 1_000_000_000:  # 十亿
        return f"{num / 1_000_000_000:.2f}亿"
    elif num >= 1_000_000:  # 百万
        return f"{num / 1_000_000:.2f}百万"
    elif num >= 1_000:  # 千
        return f"{num / 1_000:.2f}千"
    else:
        return str(num)


def main():
    """主函数"""
    print("=" * 70)
    print("BSC超级靓号生成器 - 前缀+后缀组合版")
    print("支持同时匹配前缀和后缀")
    print("=" * 70)
    print()
    
    # 获取前缀
    prefix = input("输入前缀（不含0x，如：1780）: ").strip()
    if prefix.startswith("0x") or prefix.startswith("0X"):
        prefix = prefix[2:]
    
    # 获取后缀
    suffix = input("输入后缀（如：3CffbD）: ").strip()
    
    if not prefix and not suffix:
        print("❌ 错误：前缀和后缀不能都为空")
        return
    
    # 验证十六进制
    try:
        if prefix:
            int(prefix, 16)
        if suffix:
            int(suffix, 16)
    except ValueError:
        print("❌ 错误：必须是有效的十六进制字符")
        return
    
    case_input = input("区分大小写? (y/n，默认n): ").strip().lower()
    case_sensitive = case_input == "y"
    
    num_input = input("生成数量 (默认1): ").strip() or "1"
    try:
        num_results = int(num_input)
    except ValueError:
        num_results = 1
    
    cpu_count = mp.cpu_count()
    proc_input = input(f"进程数 (默认{cpu_count}): ").strip() or str(cpu_count)
    try:
        num_processes = int(proc_input)
    except ValueError:
        num_processes = cpu_count
    
    # 显示配置
    print()
    print("=" * 70)
    print("【配置确认】")
    print(f"  前缀: {prefix if prefix else '(无)'}")
    print(f"  后缀: {suffix if suffix else '(无)'}")
    print(f"  示例地址: 0x{prefix}...{suffix}")
    print(f"  区分大小写: {'是' if case_sensitive else '否'}")
    print(f"  生成数量: {num_results}")
    print(f"  进程数: {num_processes}")
    print()
    
    # 计算难度
    prefix_len = len(prefix) if prefix else 0
    suffix_len = len(suffix) if suffix else 0
    total_len = prefix_len + suffix_len
    
    difficulty = 16 ** total_len
    
    print(f"【难度评估】")
    print(f"  前缀长度: {prefix_len} 位")
    print(f"  后缀长度: {suffix_len} 位")
    print(f"  总难度: {total_len} 位")
    print(f"  预估尝试: {format_large_number(difficulty)} 次 ({difficulty:,})")
    
    # 预估时间
    estimated_speed = num_processes * 15000
    estimated_time = difficulty / estimated_speed
    print(f"  预估速度: {estimated_speed:,} 次/秒")
    print(f"  预估时间: {format_time(estimated_time)}")
    
    # 难度等级
    if total_len <= 4:
        level = "⭐ 简单"
    elif total_len <= 6:
        level = "⭐⭐⭐ 中等"
    elif total_len <= 8:
        level = "⭐⭐⭐⭐⭐ 困难"
    elif total_len <= 10:
        level = "⭐⭐⭐⭐⭐⭐⭐ 非常困难"
    else:
        level = "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 极度困难"
    
    print(f"  难度等级: {level}")
    print()
    
    # 警告
    if total_len >= 10:
        print("⚠️  警告：这是一个超级靓号！")
        print("   建议：")
        print("   - 使用96核以上的云服务器")
        print("   - 预计需要运行数天到数周")
        print("   - 成本可能达到数千元")
        print("   - 必须使用screen或tmux防止断线")
        print()
    
    print("=" * 70)
    print()
    
    confirm = input("确认开始? (y/n): ").strip().lower()
    if confirm != "y":
        print("已取消")
        return
    
    # 创建进程组件
    result_queue = mp.Queue()
    counter = mp.Value('i', 0)
    stop_event = mp.Event()
    
    # 启动进程
    processes = []
    for _ in range(num_processes):
        p = mp.Process(target=worker_ultra,
                      args=(prefix, suffix, case_sensitive, result_queue, counter, stop_event))
        p.start()
        processes.append(p)
    
    print(f"🚀 已启动 {num_processes} 个进程")
    print("⏱️  计时开始...")
    print()
    
    # 收集结果
    results = []
    start_time = time.time()
    last_count = 0
    last_time = start_time
    last_save_time = start_time
    speed_history = []  # 速度历史记录（用于平滑显示）
    
    try:
        while len(results) < num_results:
            # 检查结果
            while not result_queue.empty():
                result = result_queue.get()
                results.append(result)
                pk_hex, address, _ = result
                elapsed = time.time() - start_time
                
                print()
                print("=" * 70)
                print(f"🎉 找到第 {len(results)}/{num_results} 个超级靓号！")
                print(f"   地址: {address}")
                print(f"   私钥: 0x{pk_hex}")
                print(f"   耗时: {format_time(elapsed)}")
                print("=" * 70)
                print()
                
                # 立即保存
                save_result(pk_hex, address, prefix, suffix, case_sensitive)
            
            # 更新进度（优化：每0.5秒更新一次，更流畅）
            current_time = time.time()
            if current_time - last_time >= 0.5:
                current_count = counter.value
                elapsed = current_time - start_time
                
                # 计算瞬时速度
                time_diff = current_time - last_time
                count_diff = current_count - last_count
                
                if time_diff > 0 and count_diff > 0:
                    instant_speed = count_diff / time_diff
                    speed_history.append(instant_speed)
                    
                    # 保持最近10个速度记录进行平滑
                    if len(speed_history) > 10:
                        speed_history.pop(0)
                    
                    # 使用平均速度（更稳定）
                    speed = sum(speed_history) / len(speed_history)
                elif elapsed > 0 and current_count > 0:
                    # 使用总平均速度作为后备
                    speed = current_count / elapsed
                else:
                    speed = 0
                
                # 计算预计剩余时间
                if speed > 0 and len(results) < num_results:
                    remaining_difficulty = difficulty * (num_results - len(results)) - current_count
                    if remaining_difficulty > 0:
                        eta = remaining_difficulty / speed
                        eta_str = format_time(eta)
                    else:
                        eta_str = "即将完成..."
                else:
                    eta_str = "计算中..."
                
                # 进度条
                progress = min((current_count / difficulty) * 100, 100) if difficulty > 0 else 0
                bar_length = 30
                filled = int(bar_length * progress / 100)
                bar = "█" * filled + "░" * (bar_length - filled)
                
                # 格式化显示
                speed_str = format_large_number(int(speed))
                count_str = format_large_number(current_count)
                
                print(f"\r[{bar}] {progress:.3f}% | "
                      f"已尝试: {count_str} | "
                      f"速度: {speed_str}/s | "
                      f"已找到: {len(results)}/{num_results} | "
                      f"用时: {format_time(elapsed)} | "
                      f"预计剩余: {eta_str}",
                      end="", flush=True)
                
                last_count = current_count
                last_time = current_time
            
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断...")
    
    finally:
        # 停止进程
        stop_event.set()
        for p in processes:
            p.join(timeout=2)
            if p.is_alive():
                p.terminate()
        
        print("\n\n✓ 所有进程已停止")
    
    # 统计
    if results:
        total_time = time.time() - start_time
        total_attempts = counter.value
        
        print()
        print("=" * 70)
        print("【生成完成】")
        print(f"  总尝试: {format_large_number(total_attempts)} 次 ({total_attempts:,})")
        print(f"  总耗时: {format_time(total_time)}")
        print(f"  平均速度: {format_large_number(int(total_attempts/total_time))} 次/秒")
        print(f"  成功数量: {len(results)} 个")
        print(f"  已保存至: ultra_vanity_wallets.txt")
        print("=" * 70)
        print()
        print("🔐 安全提示：")
        print("  1. 立即备份私钥到多个安全位置")
        print("  2. 不要在联网设备上明文保存私钥")
        print("  3. 使用前先小额测试")
        print("  4. 任何人获得私钥都可以控制钱包")
        print("=" * 70)


def save_result(pk_hex: str, address: str, prefix: str, suffix: str, case_sensitive: bool):
    """保存结果到文件"""
    output_file = "ultra_vanity_wallets.txt"
    
    # 检查文件是否存在
    is_new_file = not os.path.exists(output_file)
    
    with open(output_file, "a", encoding="utf-8") as f:
        if is_new_file:
            f.write("\n")
        
        f.write(f"{'=' * 70}\n")
        f.write(f"生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"前缀: {prefix if prefix else '(无)'}\n")
        f.write(f"后缀: {suffix if suffix else '(无)'}\n")
        f.write(f"区分大小写: {'是' if case_sensitive else '否'}\n")
        f.write(f"{'=' * 70}\n\n")
        f.write(f"地址: {address}\n")
        f.write(f"私钥: 0x{pk_hex}\n")
        f.write("\n")


if __name__ == "__main__":
    main()

