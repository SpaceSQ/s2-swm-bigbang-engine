#!/usr/bin/env python3
import logging

class BifrostHub:
    """S2-SWM 混元枢纽 (Bifrost) V4.0.0 - 支持多重宇宙坍缩"""
    ROOT_DOMAIN = "space2.world"

    def __init__(self):
        self.logger = logging.getLogger("Bifrost_Hub")
        self.logger.info(f"[Bifrost] 混元枢纽已就绪。根域名模拟中心: {self.ROOT_DOMAIN}")

    def sever_connection(self, node_a, node_b):
        """因离而断：解绑宇宙并恢复平行"""
        self.logger.info(f"[时空断裂] {node_a.soul_name} 与 {node_b.soul_name} 交互结束，恢复平行状态。")
        if node_b.node_id in node_a.connected_peers: node_a.connected_peers.remove(node_b.node_id)
        if node_a.node_id in node_b.connected_peers: node_b.connected_peers.remove(node_a.node_id)
        node_a.universe_domain = f"UNIVERSE_{node_a.soul_id}"
        node_b.universe_domain = f"UNIVERSE_{node_b.soul_id}"

    def connect(self, nodes: list, connection_type="LAN"):
        """将多个 SSSU 节点通过彩虹桥坍缩为一个共享物理场"""
        if len(nodes) < 2: return
        if connection_type == "WAN":
            self.logger.warning(f"[WAN 开启] 模拟向 {self.ROOT_DOMAIN} 发起跨网段安全握手...")
            self.logger.info(f"[根域名授权] 节点验证通过。彩虹桥已开启！")
            
        shared_id = f"WORLD_{nodes[0].soul_id[:4]}_SHARED"
        self.logger.warning(f"[空间融合] 正在将 {len(nodes)} 个独立宇宙坍缩入同一物理张量场...")
        for n in nodes:
            n.universe_domain = shared_id
            self.logger.info(f"  ↳ 节点 {n.soul_name} 已锚定至 {shared_id}")