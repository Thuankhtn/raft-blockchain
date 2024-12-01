# grpc/client.py
import grpc
import raft_pb2
import raft_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = raft_pb2_grpc.RaftServiceStub(channel)

        # Request vote
        response = stub.RequestVote(raft_pb2.RequestVoteRequest(term=1, candidate_id="node1"))
        print(f"Vote granted: {response.vote_granted}")

        # Append entries
        response = stub.AppendEntries(raft_pb2.AppendEntriesRequest(term=1, leader_id="node1", entries=["log1", "log2"]))
        print(f"Entries appended: {response.success}")

if __name__ == '__main__':
    run()
