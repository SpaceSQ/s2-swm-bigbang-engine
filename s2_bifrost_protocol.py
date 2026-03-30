#!/usr/bin/env python3
import logging

class BifrostHub:
    """S2-SWM 混元枢纽 (Bifrost) V3.1 - 本地仿真合规版"""
    ROOT_DOMAIN = "space2.world"

    def __init__(self):
        self.logger = logging.getLogger("Bifrost_Hub")
        self.logger.info(f"[Bifrost] 混元枢纽已就绪。根域名模拟中心: {self.ROOT_DOMAIN}")

    def establish_handshake(self, node_a, node_b):
        """兼容 API：双节点快速握手"""
        return self.connect([node_a, node_b], connection_type="LAN")

    def sever_connection(self, node_a, node_b):
        """兼容 API：断开连接"""
        self.logger.info(f"[时空断裂] {node_a.soul_name} 与 {node_b.soul_name} 交互结束。")
        if node_b.node_id in node_a.connected_peers:
            node_a.connected_peers.remove(node_b.node_id)
        if node_a.node_id in node_b.connected_peers:
            node_b.connected_peers.remove(node_a.node_id)
        node_a.universe_domain = f"UNIVERSE_{node_a.soul_id}"
        node_b.universe_domain = f"UNIVERSE_{node_b.soul_id}"

    def connect(self, nodes: list, connection_type="LAN"):
        """核心连接逻辑"""
        if len(nodes) < 2:
            return
        if connection_type == "WAN":
            self.logger.warning(f"[WAN 开启] 模拟向 {self.ROOT_DOMAIN} 发起跨网段安全握手...")
            self.logger.info(f"[根域名授权] 节点已通过本地沙盒验证。彩虹桥已开启！")
            self._perform_spatial_fusion(nodes, entropy_loss=0.05)
        else:
            self.logger.info(f"[LAN 直连] 检测到局域网节点，开启瞬时坍缩...")
            self._perform_spatial_fusion(nodes)

    def _perform_spatial_fusion(self, nodes, entropy_loss=0.0):
        shared_id = f"WORLD_{nodes[0].soul_id[:4]}_{nodes[1].soul_id[:4]}"
        self.logger.warning(f"[空间融合] 正在计算 {len(nodes)} 个标准单元的要素合集...")
        for n in nodes:
            n.universe_domain = shared_id