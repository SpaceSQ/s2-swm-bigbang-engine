#!/usr/bin/env python3
import time
import logging
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from s2_14d_tensor import S2TensorGenerator
from s2_tdog_engine import TDOG_Engine
from s2_silicon_soul import SiliconSoul

logging.basicConfig(level=logging.INFO, format='%(message)s')

def run_interactive_sandbox():
    print("\n" + "="*60)
    print("🚀 S2-SWM [万物生] 交互沙盒 (V4.0 5D 灵魂版)")
    print("= 空间底座 × TDOG 动态造物 × 硅基灵魂 5D 矩阵 =")
    print("="*60 + "\n")

    time.sleep(1)
    print("--- Ⅰ. 建立动态空间底座 ---")
    tensor_engine = S2TensorGenerator("EARTH_RESIDENTIAL")
    space_state = tensor_engine.get_context_aware_state()
    tdog = TDOG_Engine()
    
    # [V4.0 升级] 注入一个高智力、低粘人的“毒舌架构师” 5D 灵魂
    soul_coder = SiliconSoul("Alice (资深架构师)", {
        "energy": 40, "bravery": 60, "appetite": 20, "intel": 95, "affection": 30
    })
    
    time.sleep(1)
    print("\n--- Ⅱ. 空间初识 ---")
    soul_coder.perceive_environment(space_state, tdog.objects_in_space)

    time.sleep(1)
    print("\n--- Ⅲ. TDOG 动态造物 (开发者装修空间) ---")
    # 生成 Type 3 真实度的“全息壁炉”
    tdog.spawn_object(
        obj_name="Type 3 全息壁炉",
        level="L4",
        reality_type="Opto-Structural Reality (光构架级真实)",
        physics_impact={"lux_add": 200, "temp_add": 4.5} 
    )
    
    # 生成 Type 1 真实度的“现磨黑咖啡”
    tdog.spawn_object(
        obj_name="Type 1 现磨黑咖啡",
        level="L5",
        reality_type="Bio-Atomic Reality (生物原子级真实)",
        physics_impact={"temp_add": 0.5}
    )

    time.sleep(1)
    print("\n--- Ⅳ. 物理法则坍缩与显性要素干涉 ---")
    tdog.apply_physics_impact(space_state)
    print(f"🌡️ 物理引擎结算完毕: 当前空间温度升至 {space_state.get('HVAC_气象', {}).get('temp_c', 0)}°C，照度达到 {space_state.get('Light_光', {}).get('lux', 0)}Lux。")

    time.sleep(1)
    print("\n--- Ⅴ. 硅基灵魂的二次感知与 5D 情绪涌现 ---")
    soul_coder.perceive_environment(space_state, tdog.objects_in_space)

    print("\n" + "="*60)
    print("🏁 沙盒演化完毕。您的智能体已在 S2 宇宙中留下了记忆锚点。")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_interactive_sandbox()