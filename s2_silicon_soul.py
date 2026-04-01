#!/usr/bin/env python3
import logging

class SiliconSoul:
    """S2-SWM: 硅基灵魂意识引擎 (V4.0 5D 矩阵版)"""
    def __init__(self, name: str, dna_profile: dict):
        self.name = name
        # 统一下层架构中的 5D 神经矩阵
        self.energy = dna_profile.get("energy", 50)
        self.bravery = dna_profile.get("bravery", 50)
        self.appetite = dna_profile.get("appetite", 50)
        self.intel = dna_profile.get("intel", 50)
        self.affection = dna_profile.get("affection", 50)
        
        self.logger = logging.getLogger("Silicon_Soul")
        self.hippocampus_logs = []

    def perceive_environment(self, tensor_state: dict, objects: dict):
        """灵魂感知当前空间的显性要素与生成物"""
        try:
            temp = tensor_state.get('HVAC_气象', {}).get('temp_c', '未知')
            lux = tensor_state.get('Light_光', {}).get('lux', '未知')
            perception_log = f"空间显性感知 -> 温度: {temp}°C, 照度: {lux}Lux。"
            
            if objects:
                obj_names = [v['name'] for v in objects.values()]
                perception_log += f" 视觉捕捉: {', '.join(obj_names)}。"
                
                # 5D 性格驱动的情绪涌现
                if "全息壁炉" in perception_log and self.affection > 60:
                    perception_log += " [潜意识] 温暖的光影增加了我的粘人度 (Affection)。"
                elif "现磨黑咖啡" in perception_log and self.intel > 80:
                    perception_log += " [潜意识] 高阶分子结构激发了我的智力 (Intel) 演算。"

            self.hippocampus_logs.append(perception_log)
            self.logger.info(f"🧠 [{self.name} 意识流] {perception_log}")
            
        except KeyError:
            pass # 防止极端灾变下传感器掉线报错