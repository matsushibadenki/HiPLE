# /hybrid_llm_system/utils/monitoring.py
# システムリソース（メモリ、CPU）を監視するためのユーティリティ

import psutil
import os

def print_memory_usage(context: str = "CURRENT") -> None:
    """
    現在のプロセスのメモリ使用状況を詳細に表示する
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    
    # メガバイト単位に変換
    rss_mb = mem_info.rss / (1024 * 1024)
    vms_mb = mem_info.vms / (1024 * 1024)
    
    print(
        f"--- 📊 Memory Usage ({context}) ---\n"
        f"  - RSS: {rss_mb:.2f} MB (物理メモリ)\n"
        f"  - VMS: {vms_mb:.2f} MB (仮想メモリ)\n"
        f"------------------------------------"
    )