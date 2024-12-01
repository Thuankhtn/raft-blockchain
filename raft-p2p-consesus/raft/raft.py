# raft/raft.py
class Raft:
    def __init__(self):
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.commit_index = 0
        self.state = "Follower"  # "Leader", "Candidate"

    def request_vote(self, term, candidate_id):
        if term > self.current_term:
            self.current_term = term
            self.state = "Follower"

        if self.voted_for is None or self.voted_for == candidate_id:
            self.voted_for = candidate_id
            return True
        return False

    def append_entries(self, entries):
        self.log.extend(entries)
        self.commit_index = len(self.log) - 1
        print(f"Entries appended: {entries}")
