#!/usr/bin/env python3
import logging

class S2TensorGenerator:
    """S2-SWM: 14 维度物理场全息张量生成器"""
    
    def __init__(self, env_mode="EARTH_RESIDENTIAL"):
        self.mode = env_mode
        self.logger = logging.getLogger("S2_Tensor")

    def generate_raw_tensor(self):
        """生成物理世界的底层 14 维参数底座"""
        return {
            # --- 核心 6 要素 (Core 6) ---
            "Light_光": {"lux": 300, "color_temp": 4000},
            "HVAC_气象": {"temp_c": 24.0, "humidity": 50, "pm25": 10},
            "Sound_声": {"noise_db": 30, "bgm": "None"},
            "EM_电磁波": {"wifi_signal_dbm": -50, "radar_occupancy": False},
            "Energy_能": {"power_watt": 150, "voltage": 220},
            "Vision_视": {"display_active": False, "camera_stream": "None"},
            
            # --- 隐性/极限 8 要素 (Implicit 8) ---
            "Air_空气": {"o2_percent": 21.0, "co2_ppm": 400},
            "Pressure_气压": {"kpa": 101.325}, 
            "Odor_气味": {"scent": "Neutral", "intensity": 0},
            "Tactile_触觉": {"vibration_hz": 0, "haptic_feedback": False},
            "Magnetic_磁场": {"geomagnetic_active": True},
            "Gravity_重力": {"g_force": 9.8}, 
            "Water_水": {"flow_rate_Lpm": 0, "potable": True},
            "Food_食物": {"calories_available": 0}
        }

    def get_context_aware_state(self):
        """触发环境感知开关，返回对应维度的物理状态"""
        raw_tensor = self.generate_raw_tensor()
        
        if self.mode == "EARTH_RESIDENTIAL":
            # 降维截断：地球民用建筑仅暴露核心 6 要素
            filtered = {k: v for k, v in raw_tensor.items() if k in [
                "Light_光", "HVAC_气象", "Sound_声", "EM_电磁波", "Energy_能", "Vision_视"
            ]}
            return filtered
        else:
            # 宇宙模式：全量 14 维展开
            return raw_tensor