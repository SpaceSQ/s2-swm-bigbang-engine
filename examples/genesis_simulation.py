#!/usr/bin/env python3
import sys
import os
import time
import logging

# 确保能导入外层目录的核心引擎代码
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from s2_sssu_node import SSSUNode
from s2_bifrost_protocol import BifrostHub
from s2_causal_dynamics import BigBangEngine  # [V4.0 引入大爆炸引擎]

logging.basicConfig(level=logging.INFO, format='%(message)s')

def run_causal_multiverse_demo():
    print("\n" + "="*60)
    print("🚀 S2-SWM 宇宙大爆炸演化沙盒 (V4.0.0 因果动力学版)")
    print("="*60 + "\n")
    
    time.sleep(1)
    # 1. 生成三个独立的平行宇宙
    print("--- 阶段 I: 平行宇宙诞生 ---")
    node_earth = SSSUNode(soul_name="Alpha_地球实验室", env_mode="EARTH_RESIDENTIAL")
    node_mars = SSSUNode(soul_name="Beta_火星栖息舱", env_mode="DEEP_SPACE")
    node_station = SSSUNode(soul_name="Gamma_近地空间站", env_mode="DEEP_SPACE")
    
    time.sleep(1)
    # 2. 随需连接：平行宇宙通过彩虹桥坍缩为一个共享物理场
    print("\n--- 阶段 II: 广域网彩虹桥连接 (时空坍缩) ---")
    hub = BifrostHub()
    worlds_to_merge = [node_earth, node_mars, node_station]
    hub.connect(worlds_to_merge, connection_type="WAN")
    
    # 获取融合后的共享宇宙 ID
    shared_universe_id = node_earth.universe_domain 
    
    time.sleep(1)
    # 3. 启动 V4.0 大爆炸引擎，接管这个共享宇宙的物理法则
    print(f"\n--- 阶段 III: 大爆炸引擎接管共享时空 [{shared_universe_id}] ---")
    causal_engine = BigBangEngine(space_id=shared_universe_id)
    causal_engine.register_life("Silicon", node_earth.soul_name, "Active_Computing")
    causal_engine.register_life("Silicon", node_mars.soul_name, "Standby")
    causal_engine.register_life("Silicon", node_station.soul_name, "Standby")

    # 模拟物理时间的流逝
    for t in range(1, 4):
        print(f"\n⏳ [物理时空 Tick {t}] ------------------------------")
        
        external_shock = None
        if t == 2:
            print("☄️ [突发因果事件] 火星舱遭遇微流星体穿透！物理张量出现局部崩塌！")
            # 外部物理灾变输入：火星气压暴跌，流体矢量（狂风）暴增
            external_shock = {"Barometric_Tide": 300.5, "Fluid_Dynamic_Vector": 15.0} 

        # 引擎步进，计算因果纠缠与空间信息熵
        impact_logs = causal_engine.tick(external_shock)
        
        # 打印当前共享宇宙的宏观物理状态
        print(f"🌡️ 共享热辐射通量: {causal_engine.tensor_matrix['Thermal_Flux']:.2f} W/m2")
        print(f"🌪️ 共享流体矢量: {causal_engine.tensor_matrix['Fluid_Dynamic_Vector']:.2f} m/s")
        print(f"📈 共享空间信息熵: {causal_engine.tensor_matrix['Spatial_Entropy']:.4f}")
        
        # 打印物理灾变对所有连通宇宙中生命体的影响
        for log in impact_logs:
            print(log)
            
        time.sleep(1.5)

    print("\n" + "="*60)
    print("🏁 沙盒推演完毕。S2-SWM 跨时空因果律已闭环。")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_causal_multiverse_demo()