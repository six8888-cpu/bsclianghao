#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
超级靓号生成器 V2 - 增强版
新增功能：概率显示、详细统计、运气评估、彩色输出
"""

import os
import time
import secrets
import multiprocessing as mp
from typing import Tuple, Optional
from eth_utils import to_checksum_address
from Crypto.Hash import keccak
from eth_keys import keys
import math


# ANSI颜色代码
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'


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


def check_pattern_combined(address: str, prefix: str, suffix: str, contains: str, case_sensitive: bool) -> bool:
    """检查前缀+后缀+包含的组合匹配"""
    addr = address[2:]
    
    if not case_sensitive:
        addr = addr.lower()
        if prefix:
            prefix = prefix.lower()
        if suffix:
            suffix = suffix.lower()
        if contains:
            contains = contains.lower()
    
    # 检查所有条件
    if prefix and not addr.startswith(prefix):
        return False
    if suffix and not addr.endswith(suffix):
        return False
    if contains and contains not in addr:
        return False
    
    return True


def worker_ultra(prefix: str, suffix: str, contains: str, case_sensitive: bool,
                result_queue: mp.Queue, counter: mp.Value, stop_event: mp.Event, stats_queue: mp.Queue):
    """超级靓号工作进程（V2增强版）- 支持前缀+后缀+包含组合"""
    local_count = 0
    local_speed_samples = []
    last_update = time.time()
    
    while not stop_event.is_set():
        try:
            private_key = secrets.token_bytes(32)
            pk_hex, address = generate_address_fast(private_key)
            
            local_count += 1
            
            # 每1000次更新一次计数器
            if local_count % 1000 == 0:
                with counter.get_lock():
                    counter.value += 1000
                
                # 计算本地速度并发送统计
                current_time = time.time()
                time_diff = current_time - last_update
                if time_diff > 0:
                    local_speed = 1000 / time_diff
                    if not stats_queue.full():
                        stats_queue.put(('speed', local_speed))
                last_update = current_time
            
            # 检查匹配（支持前缀+后缀+包含的任意组合）
            if check_pattern_combined(address, prefix, suffix, contains, case_sensitive):
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
    if num >= 1_000_000_000_000:
        return f"{num / 1_000_000_000_000:.2f}万亿"
    elif num >= 1_000_000_000:
        return f"{num / 1_000_000_000:.2f}亿"
    elif num >= 1_000_000:
        return f"{num / 1_000_000:.2f}百万"
    elif num >= 1_000:
        return f"{num / 1_000:.2f}千"
    else:
        return str(num)


def calculate_probability(attempts: int, difficulty: int) -> float:
    """计算已找到的概率"""
    if difficulty == 0:
        return 0
    # 使用概率公式: P = 1 - (1 - 1/N)^n
    # 近似: P ≈ 1 - e^(-n/N)
    ratio = attempts / difficulty
    probability = 1 - math.exp(-ratio)
    return probability * 100


def get_luck_status(probability: float) -> Tuple[str, str]:
    """获取运气状态"""
    if probability < 5:
        return Colors.CYAN, "😎 才刚开始"
    elif probability < 20:
        return Colors.GREEN, "🍀 运气不错"
    elif probability < 40:
        return Colors.GREEN, "✨ 进展顺利"
    elif probability < 60:
        return Colors.YELLOW, "💫 稳步推进"
    elif probability < 80:
        return Colors.YELLOW, "⏳ 快了快了"
    elif probability < 95:
        return Colors.RED, "💪 坚持住"
    else:
        return Colors.RED + Colors.BOLD, "🔥 马上就要出了"


def main():
    """主函数"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}BSC超级靓号生成器 V2 - 增强版{Colors.RESET}")
    print(f"{Colors.CYAN}新增：概率显示 | 详细统计 | 运气评估 | 彩色输出{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 70}{Colors.RESET}\n")
    
    # 灵活的配置方式
    print(f"{Colors.BOLD}【灵活配置】{Colors.RESET}")
    print(f"{Colors.CYAN}提示：不需要的条件直接按回车跳过{Colors.RESET}\n")
    
    # 1. 询问前缀
    prefix = input(f"{Colors.YELLOW}前缀（如: 1780，不需要按回车跳过）: {Colors.RESET}").strip()
    if prefix.startswith("0x") or prefix.startswith("0X"):
        prefix = prefix[2:]
    
    # 2. 询问后缀
    suffix = input(f"{Colors.YELLOW}后缀（如: 3CffbD，不需要按回车跳过）: {Colors.RESET}").strip()
    
    # 3. 询问包含
    contains = input(f"{Colors.YELLOW}包含（如: 888，不需要按回车跳过）: {Colors.RESET}").strip()
    
    # 检查至少有一个条件
    if not prefix and not suffix and not contains:
        print(f"\n{Colors.RED}❌ 错误：至少需要一个匹配条件（前缀/后缀/包含）{Colors.RESET}")
        return
    
    # 验证十六进制
    try:
        if prefix:
            int(prefix, 16)
        if suffix:
            int(suffix, 16)
        if contains:
            int(contains, 16)
    except ValueError:
        print(f"\n{Colors.RED}❌ 错误：必须是有效的十六进制字符（0-9, a-f）{Colors.RESET}")
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
    print(f"\n{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(f"{Colors.BOLD}【配置确认】{Colors.RESET}")
    print(f"  前缀: {Colors.YELLOW}{prefix if prefix else '(无)'}{Colors.RESET}")
    print(f"  后缀: {Colors.YELLOW}{suffix if suffix else '(无)'}{Colors.RESET}")
    print(f"  包含: {Colors.YELLOW}{contains if contains else '(无)'}{Colors.RESET}")
    
    # 生成示例地址
    example_parts = []
    if prefix:
        example_parts.append(prefix)
    example_parts.append("...")
    if contains:
        example_parts.append(f"{contains}...")
    if suffix:
        example_parts.append(suffix)
    example_addr = "0x" + "".join(example_parts)
    print(f"  示例: {Colors.GREEN}{example_addr}{Colors.RESET}")
    
    print(f"  区分大小写: {'是' if case_sensitive else '否'}")
    print(f"  生成数量: {num_results}")
    print(f"  进程数: {num_processes}")
    print()
    
    # 计算难度（前缀+后缀的组合难度，包含模式单独计算）
    prefix_len = len(prefix) if prefix else 0
    suffix_len = len(suffix) if suffix else 0
    contains_len = len(contains) if contains else 0
    
    # 前缀+后缀是确定位置，难度累加
    fixed_len = prefix_len + suffix_len
    if fixed_len > 0:
        difficulty = 16 ** fixed_len
    else:
        difficulty = 1
    
    # 包含模式是不确定位置，难度按平均估算（地址40位，滑动窗口）
    if contains_len > 0:
        # 包含模式的难度约为 16^n / (40 - n + 1)
        contains_difficulty = 16 ** contains_len / max(1, 40 - contains_len)
        if fixed_len > 0:
            # 如果有固定位置，难度相乘
            difficulty *= contains_difficulty
        else:
            difficulty = contains_difficulty
    
    print(f"{Colors.BOLD}【难度评估】{Colors.RESET}")
    print(f"  前缀: {prefix_len}位 | 后缀: {suffix_len}位 | 包含: {contains_len}位")
    print(f"  总难度: {Colors.BOLD}{prefix_len + suffix_len + contains_len}位{Colors.RESET}")
    print(f"  预估尝试: {Colors.YELLOW}{format_large_number(int(difficulty))}{Colors.RESET} 次")
    
    estimated_speed = num_processes * 15000
    estimated_time = difficulty / estimated_speed
    print(f"  预估速度: {format_large_number(estimated_speed)} 次/秒")
    print(f"  预估时间: {Colors.CYAN}{format_time(estimated_time)}{Colors.RESET}")
    print()
    
    total_difficulty_len = prefix_len + suffix_len + contains_len
    if total_difficulty_len >= 10:
        print(f"{Colors.RED}⚠️  警告：这是一个超级靓号！预计需要很长时间{Colors.RESET}")
        print()
    
    print(f"{'=' * 70}\n")
    
    confirm = input(f"{Colors.BOLD}确认开始? (y/n): {Colors.RESET}").strip().lower()
    if confirm != "y":
        print("已取消")
        return
    
    # 创建队列
    result_queue = mp.Queue()
    counter = mp.Value('i', 0)
    stop_event = mp.Event()
    stats_queue = mp.Queue(maxsize=1000)
    
    # 启动进程
    processes = []
    for _ in range(num_processes):
        p = mp.Process(target=worker_ultra,
                      args=(prefix, suffix, contains, case_sensitive, result_queue, counter, stop_event, stats_queue))
        p.start()
        processes.append(p)
    
    print(f"\n{Colors.GREEN}🚀 已启动 {num_processes} 个进程{Colors.RESET}")
    print(f"{Colors.GREEN}⏱️  计时开始...{Colors.RESET}\n")
    
    # 收集结果
    results = []
    start_time = time.time()
    last_count = 0
    last_time = start_time
    speed_history = []
    max_speed = 0
    total_speed_samples = 0
    speed_sample_count = 0
    
    try:
        while len(results) < num_results:
            # 检查结果
            while not result_queue.empty():
                result = result_queue.get()
                results.append(result)
                pk_hex, address, _ = result
                elapsed = time.time() - start_time
                
                print(f"\n\n{Colors.BOLD}{Colors.GREEN}{'=' * 70}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.GREEN}🎉 找到第 {len(results)}/{num_results} 个超级靓号！{Colors.RESET}")
                print(f"{Colors.BOLD}   地址: {Colors.YELLOW}{address}{Colors.RESET}")
                print(f"   私钥: {Colors.CYAN}0x{pk_hex}{Colors.RESET}")
                print(f"   耗时: {Colors.PURPLE}{format_time(elapsed)}{Colors.RESET}")
                print(f"{Colors.GREEN}{'=' * 70}{Colors.RESET}\n")
                
                save_result(pk_hex, address, prefix, suffix, contains, case_sensitive)
            
            # 处理统计数据
            while not stats_queue.empty():
                try:
                    stat_type, stat_value = stats_queue.get_nowait()
                    if stat_type == 'speed':
                        total_speed_samples += stat_value
                        speed_sample_count += 1
                except:
                    pass
            
            # 更新进度
            current_time = time.time()
            if current_time - last_time >= 0.5:
                current_count = counter.value
                elapsed = current_time - start_time
                
                # 计算速度
                time_diff = current_time - last_time
                count_diff = current_count - last_count
                
                if time_diff > 0 and count_diff > 0:
                    instant_speed = count_diff / time_diff
                    speed_history.append(instant_speed)
                    
                    if len(speed_history) > 10:
                        speed_history.pop(0)
                    
                    speed = sum(speed_history) / len(speed_history)
                    max_speed = max(max_speed, speed)
                elif elapsed > 0 and current_count > 0:
                    speed = current_count / elapsed
                else:
                    speed = 0
                
                # 计算概率
                probability = calculate_probability(current_count, difficulty)
                luck_color, luck_status = get_luck_status(probability)
                
                # 计算预计剩余时间
                if speed > 0 and len(results) < num_results:
                    remaining_difficulty = difficulty * (num_results - len(results)) - current_count
                    if remaining_difficulty > 0:
                        eta = remaining_difficulty / speed
                        eta_str = format_time(eta)
                    else:
                        eta_str = "即将完成"
                else:
                    eta_str = "计算中"
                
                # 进度条
                progress = min((current_count / difficulty) * 100, 100) if difficulty > 0 else 0
                bar_length = 30
                filled = int(bar_length * progress / 100)
                bar = "█" * filled + "░" * (bar_length - filled)
                
                # 显示信息
                speed_str = format_large_number(int(speed))
                count_str = format_large_number(current_count)
                
                print(f"\r{Colors.CYAN}[{bar}] {progress:.2f}%{Colors.RESET} | "
                      f"已尝试: {Colors.YELLOW}{count_str}{Colors.RESET} | "
                      f"速度: {Colors.GREEN}{speed_str}/s{Colors.RESET} | "
                      f"概率: {luck_color}{probability:.1f}%{Colors.RESET} | "
                      f"{luck_color}{luck_status}{Colors.RESET} | "
                      f"预计: {Colors.PURPLE}{eta_str}{Colors.RESET}",
                      end="", flush=True)
                
                last_count = current_count
                last_time = current_time
            
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠️  用户中断...{Colors.RESET}")
    
    finally:
        stop_event.set()
        for p in processes:
            p.join(timeout=2)
            if p.is_alive():
                p.terminate()
        
        print(f"\n\n{Colors.GREEN}✓ 所有进程已停止{Colors.RESET}")
    
    # 统计
    if results:
        total_time = time.time() - start_time
        total_attempts = counter.value
        avg_speed = total_attempts / total_time if total_time > 0 else 0
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'=' * 70}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}【生成完成】{Colors.RESET}")
        print(f"  总尝试: {Colors.YELLOW}{format_large_number(total_attempts)}{Colors.RESET} 次 ({total_attempts:,})")
        print(f"  总耗时: {Colors.PURPLE}{format_time(total_time)}{Colors.RESET}")
        print(f"  平均速度: {Colors.GREEN}{format_large_number(int(avg_speed))}{Colors.RESET} 次/秒")
        print(f"  峰值速度: {Colors.CYAN}{format_large_number(int(max_speed))}{Colors.RESET} 次/秒")
        print(f"  成功数量: {Colors.BOLD}{len(results)}{Colors.RESET} 个")
        
        # 运气评估
        final_probability = calculate_probability(total_attempts, difficulty)
        if final_probability < 50:
            luck_msg = f"{Colors.GREEN}🍀 运气超好！提前完成！{Colors.RESET}"
        elif final_probability < 70:
            luck_msg = f"{Colors.GREEN}✨ 运气不错，正常完成{Colors.RESET}"
        elif final_probability < 90:
            luck_msg = f"{Colors.YELLOW}💫 正常范围，按时完成{Colors.RESET}"
        else:
            luck_msg = f"{Colors.YELLOW}💪 有点背运，但还在正常范围{Colors.RESET}"
        
        print(f"  运气评估: {luck_msg}")
        print(f"  保存位置: {Colors.CYAN}ultra_vanity_wallets.txt{Colors.RESET}")
        print(f"{Colors.GREEN}{'=' * 70}{Colors.RESET}\n")
        print(f"{Colors.BOLD}🔐 安全提示：{Colors.RESET}")
        print("  1. 立即备份私钥到多个安全位置")
        print("  2. 不要在联网设备上明文保存私钥")
        print("  3. 使用前先小额测试")
        print("  4. 任何人获得私钥都可以控制钱包")
        print(f"{Colors.GREEN}{'=' * 70}{Colors.RESET}\n")


def save_result(pk_hex: str, address: str, prefix: str, suffix: str, contains: str, case_sensitive: bool):
    """保存结果"""
    output_file = "ultra_vanity_wallets.txt"
    
    is_new_file = not os.path.exists(output_file)
    
    with open(output_file, "a", encoding="utf-8") as f:
        if is_new_file:
            f.write("\n")
        
        f.write(f"{'=' * 70}\n")
        f.write(f"生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"前缀: {prefix if prefix else '(无)'}\n")
        f.write(f"后缀: {suffix if suffix else '(无)'}\n")
        f.write(f"包含: {contains if contains else '(无)'}\n")
        f.write(f"区分大小写: {'是' if case_sensitive else '否'}\n")
        f.write(f"{'=' * 70}\n\n")
        f.write(f"地址: {address}\n")
        f.write(f"私钥: 0x{pk_hex}\n")
        f.write("\n")


if __name__ == "__main__":
    main()

