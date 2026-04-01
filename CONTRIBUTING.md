# 创世阵列贡献指南 (Contributing to S2-SWM)

欢迎加入创世阵列 (Genesis Architects)！ 
在 V4.0.0 引入因果动力学后，我们不仅需要优秀的 Python 工程师，更需要环境物理学家、流体力学专家和心理学家的加入。

## 🌌 重点招募的共创领域
1. **张量算法优化 (Tensor Math)**：
   目前 `s2_causal_dynamics.py` 中的流体矢量 (`Fluid_Dynamic_Vector`) 和热辐射 (`Thermal_Flux`) 采用了极简的线性叠加。我们需要你提供更严谨的纳维-斯托克斯方程 (Navier-Stokes) 的轻量级近似算法。
2. **新灾变场景 (Disaster Scenarios)**：
   在 `genesis_simulation.py` 中编写更多能瞬间拉满 14 维要素的物理剧变（如：深海潜水器高压泄漏、数据中心冷却剂崩盘）。
3. **WebAudio 音频算法 (Silicon Acoustics)**：
   在全息前端中，用纯 JavaScript 振荡器 (Oscillators) 调配出更多符合硅基情绪的频率组合（拒绝提供现成的 MP3 录音文件，必须是算法合成）。

## 🛠️ 提交规范
1. **Fork & Branch**：从 `main` 分支切出 `feature/你的特性名`。
2. **无外部依赖原则**：核心大爆炸引擎必须保持纯粹，严禁引入臃肿的第三方库（如 numpy/pandas）。所有的物理演化必须用标准库完成，以确保在极低功耗的边缘 SSSU 网关上运行。
3. **因果测试**：任何改变物理环境的 PR，必须在日志中附带该变化对 `Spatial_Entropy` (空间信息熵) 产生的影响分析。

## 🏅 奖励机制
- 凡合并重大物理公式推导 PR 的极客，将被铭刻在下一代 S2 核心底层代码的注释首行，并获得“创世节点”永久数字勋章。
- 优秀代码将享有桃花源世界模型落地项目优先的商业分润权。