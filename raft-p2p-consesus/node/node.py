from grpc import server
from raft.election import start_election
from raft.log import sync_logs
from grpc.server import RaftService
from node.node_config import NODE_CONFIG

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.config = NODE_CONFIG[node_id]
        self.state = "follower"  # Trạng thái ban đầu
    
    def run_server(self):
        # Khởi động server gRPC cho nút này
        grpc_server = server.Server()
        grpc_server.add_insecure_port(f'{self.config["address"]}:{self.config["port"]}')
        grpc_server.start()
        print(f"Node {self.node_id} is running...")
        grpc_server.wait_for_termination()
    
    def handle_vote_request(self):
        # Xử lý yêu cầu bầu chọn (RequestVote)
        pass

    def handle_append_entries(self):
        # Xử lý yêu cầu đồng bộ log (AppendEntries)
        pass
