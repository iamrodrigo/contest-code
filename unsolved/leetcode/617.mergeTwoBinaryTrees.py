# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution(object):
    def mergeTrees(self, t1, t2):
        t1queue = collections.deque([t1])
        t2queue = collections.deque([t2])
        counter = -1

        newTreeQueue = collections.deque()
        root = None

        while len(t1queue) or len(t2queue):

            node = None
            counter += 1

            t1Node = t1queue.popleft() if len(t1queue) else None
            t2Node = t2queue.popleft() if len(t2queue) else None

            nodesSum = None

            if t1Node and t2Node:
                nodesSum = t1Node.val + t2Node.val
            elif t1Node and not t2Node:
                nodesSum = t1Node.val
            elif t2Node and not t1Node:
                nodesSum = t2Node.val

            if nodesSum is not None:
                node = TreeNode(nodesSum)
                newTreeQueue.append(node)

            if counter == 0:
                root = node
            elif counter == 1:
                newTreeQueue[0].left = node
            else:
                newTreeQueue[0].right = node
                counter = 0
                newTreeQueue.popleft()

            if t1Node or t2Node:
                t1queue.append(t1Node.left if t1Node else None)
                t1queue.append(t1Node.right if t1Node else None)
                t2queue.append(t2Node.left if t2Node else None)
                t2queue.append(t2Node.right if t2Node else None)

        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

s = Solution()
p = s.mergeTrees(root, root2)
pass