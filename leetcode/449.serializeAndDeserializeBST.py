import collections

class Codec:
    def serialize(self, root):
        serialized = ''
        nodesQueue = collections.deque([root])

        while len(nodesQueue):
            node = nodesQueue.popleft()
            val = '#'
            if node:
                nodesQueue.append(node.left)
                nodesQueue.append(node.right)
                val = node.val

            serialized += str(val) + '-'

        return serialized[0:-1]

    def deserialize(self, data):
        nodesQueue = collections.deque()
        root = None
        treeString = data.split('-')
        counter = -1

        for value in treeString:
            counter += 1
            node = None

            if value != '#':
                node = TreeNode(value)
                nodesQueue.append(node)

            if counter == 0:
                root = node
            elif counter == 1:
                nodesQueue[0].left = node
            elif counter == 2:
                nodesQueue[0].right = node
                counter = 0
                nodesQueue.popleft()

        return root