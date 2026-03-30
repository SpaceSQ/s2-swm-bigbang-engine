#!/usr/bin/env python3
from s2_sssu_node import SSSUNode
from s2_bifrost_protocol import BifrostHub
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def run_wan_fusion_demo():
    hub = BifrostHub()

    # 1. 创建三个处于不同维度的世界 (模拟跨网段)
    node_a = SSSUNode("Alpha_实验室", env_mode="EARTH_RESIDENTIAL")
    node_b = SSSUNode("Beta_火星舱", env_mode="DEEP_SPACE")
    node_c = SSSUNode("Gamma_空间站", env_mode="DEEP_SPACE")

    # 2. 预设不同的物理状态
    node_a.mutate_reality("HVAC_气象", "temp_c", 20.0)
    node_b.mutate_reality("HVAC_气象", "temp_c", 10.0)
    node_c.mutate_reality("HVAC_气象", "temp_c", 15.0)

    print("\n--- 🌐 场景：发起广域网彩虹桥连接 ---")
    # 3. 指定通过根域名 space2.world 进行跨网段融合
    worlds_to_merge = [node_a, node_b, node_c]
    hub.connect(worlds_to_merge, connection_type="WAN")

    # 4. 验证 14 要素计算结果
    print(f"\n--- 🧪 14要素融合结果验证 ---")
    print(f"Alpha 世界温度: {node_a.physics_state['HVAC_气象']['temp_c']}°C")
    print(f"Beta  世界温度: {node_b.physics_state['HVAC_气象']['temp_c']}°C")
    print(f"Gamma 世界温度: {node_c.physics_state['HVAC_气象']['temp_c']}°C")

if __name__ == "__main__":
    run_wan_fusion_demo()