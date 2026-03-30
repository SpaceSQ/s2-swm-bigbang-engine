#!/usr/bin/env python3
import sys
import os
import time
import logging

# 确保能导入外层目录的核心引擎代码
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from s2_sssu_node import SSSUNode
from s2_bifrost_protocol import BifrostHub

logging.basicConfig(level=logging.INFO, format='%(message)s')

def run_genesis_simulation():
    print("\n" + "="*50)
    print("🚀 S2-SWM 宇宙大爆炸演化沙盒启动")
    print("="*50 + "\n")
    
    time.sleep(1)
    # 1. 生成两个独立的平行宇宙
    print("--- 阶段 I: 平行宇宙诞生 ---")
    node_alice = SSSUNode(soul_name="Alice_地球", env_mode="EARTH_RESIDENTIAL")
    node_bob = SSSUNode(soul_name="Bob_火星", env_mode="DEEP_SPACE")
    
    time.sleep(1)
    # 2. 局部法则修改
    print("\n--- 阶段 II: 主观能动性修正 ---")
    node_bob.mutate_reality("Gravity_重力", "g_force", 3.72) # 修改重力
    node_bob.mutate_reality("HVAC_气象", "temp_c", 10.5)     # 火星舱温度调低
    
    time.sleep(1)
    # 3. 随需连接：平行宇宙坍缩
    print("\n--- 阶段 III: Bifrost 协议握手 ---")
    hub = BifrostHub()
    hub.establish_handshake(node_alice, node_bob)
    
    time.sleep(1)
    # 4. 因离而断：宇宙解绑并恢复平行
    print("\n--- 阶段 IV: 因离而断 ---")
    hub.sever_connection(node_alice, node_bob)
    
    print("\n" + "="*50)
    print("🏁 沙盒推演完毕。S2-SWM 因果律已闭环。")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_genesis_simulation()