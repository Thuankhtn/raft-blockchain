# test/test_raft.py
import unittest
from raft.raft import Raft

class TestRaft(unittest.TestCase):

    def test_request_vote(self):
        raft = Raft()
        self.assertTrue(raft.request_vote(1, "node1"))
        self.assertFalse(raft.request_vote(0, "node2"))

    def test_append_entries(self):
        raft = Raft()
        raft.append_entries(["log1", "log2"])
        self.assertEqual(len(raft.log), 2)
        self.assertEqual(raft.log[-1], "log2")

if __name__ == '__main__':
    unittest.main()
