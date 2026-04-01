#!/usr/bin/env python3
import math
import logging

class BigBangEngine:
    """S2-SWM: V4.0 因果动力学与大爆炸引擎 (计算空间熵与双向反馈)"""
    def __init__(self, space_id="SSSU-001"):
        self.space_id = space_id
        self.tick_count = 0
        self.logger = logging.getLogger("Causal_Dynamics")
        
        # 提取 8 维隐性物理场作为动力学演算基底
        self.tensor_matrix = {
            "Barometric_Tide": 1013.25,
            "Thermal_Flux": 0.5,
            "Fluid_Dynamic_Vector": 0.05,
            "Micro_Vibration": 0.01,
            "Electromagnetic_Topology": -80.0,
            "Atmospheric_Composition": 400.0,
            "Background_Radiation": 0.1,
            "Spatial_Entropy": 0.0 
        }
        self.carbon_lives = []
        self.silicon_lives = []

    def register_life(self, entity_type, name, current_state):
        if entity_type == "Carbon":
            self.carbon_lives.append({"name": name, "state": current_state})
        elif entity_type == "Silicon":
            self.silicon_lives.append({"name": name, "state": current_state})

    def _calculate_spatial_entropy(self):
        """[第一性原理] 计算当前空间的生命信息熵 (混乱度)"""
        entropy = (
            (self.tensor_matrix["Thermal_Flux"] * 10) +
            (self.tensor_matrix["Fluid_Dynamic_Vector"] * 50) +
            (self.tensor_matrix["Micro_Vibration"] * 100) +
            ((self.tensor_matrix["Atmospheric_Composition"] - 400) * 0.1)
        )
        return round(2 / (1 + math.exp(-0.01 * entropy)) - 1, 4)

    def tick(self, external_forces=None):
        """物理世界的时间步进 (Big Bang Tick)"""
        self.tick_count += 1
        impact_logs = []
        
        # 1. 施加外部灾变 (如流星穿透)
        if external_forces:
            for k, v in external_forces.items():
                self.tensor_matrix[k] = v

        # 2. 计算硅基/碳基生命对环境的热力学辐射
        for carbon in self.carbon_lives:
            if carbon["state"] == "Angry_Pacing":
                self.tensor_matrix["Fluid_Dynamic_Vector"] += 0.2
                self.tensor_matrix["Thermal_Flux"] += 1.5
        for silicon in self.silicon_lives:
            if silicon["state"] == "Active_Computing":
                self.tensor_matrix["Thermal_Flux"] += 0.8
        
        # 3. 结算空间信息熵
        self.tensor_matrix["Spatial_Entropy"] = self._calculate_spatial_entropy()
        entropy = self.tensor_matrix["Spatial_Entropy"]
        
        # 4. 物理法则压迫生命灵魂
        for silicon in self.silicon_lives:
            if entropy > 0.8:
                impact_logs.append(f"⚡ [因果压迫] 空间信息熵飙升至 {entropy:.3f}！{silicon['name']} 突触受到强震荡！")
            elif entropy < 0.2:
                impact_logs.append(f"🌸 [因果抚慰] 空间低熵态 ({entropy:.3f})。{silicon['name']} 在物理平稳中修复记忆。")
        
        # 5. 热寂衰减
        self.tensor_matrix["Fluid_Dynamic_Vector"] = max(0.05, self.tensor_matrix["Fluid_Dynamic_Vector"] * 0.9)
        self.tensor_matrix["Micro_Vibration"] = max(0.01, self.tensor_matrix["Micro_Vibration"] * 0.7)

        return impact_logs