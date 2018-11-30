# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if not root:
            return '#'

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return '{}-{}-{}'.format(root.val, left, right)

    def deserialize(self, data):
        nodesStack = []
        root = None
        treeString = data.split('-')
        for value in treeString:
            if value != '#':
                node = TreeNode(value)
                if len(nodesStack):
                    parent = nodesStack[-1] if nodesStack[-1] != '#' else nodesStack[-2]

                    if value > parent.val:
                        parent.right = node
                    else:
                        parent.left = node

                else:
                    root = node
                nodesStack.append(node)
            else:
                nodesStack.append('#')
                while len(nodesStack) > 1 and nodesStack[-1] == '#' and nodesStack[-2] == '#':
                    nodesStack.pop()
                    nodesStack.pop()
                    nodesStack.pop()
                    nodesStack.append('#')

        return root


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

s = Codec()
s.deserialize(s.serialize(root))
pass