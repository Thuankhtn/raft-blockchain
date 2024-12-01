# grpc/server.py
import grpc
from concurrent import futures
import raft_pb2
import raft_pb2_grpc
from raft.raft import Raft

class RaftService(raft_pb2_grpc.RaftServiceServicer):
    def __init__(self):
        self.raft = Raft()

    def RequestVote(self, request, context):
        result = self.raft.request_vote(request.term, request.candidate_id)
        return raft_pb2.RequestVoteResponse(vote_granted=result)

    def AppendEntries(self, request, context):
        self.raft.append_entries(request.entries)
        return raft_pb2.AppendEntriesResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    raft_pb2_grpc.add_RaftServiceServicer_to_server(RaftService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
