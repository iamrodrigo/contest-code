from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        vertexList = [0] * len(rooms)

        q = deque([0])

        while q:
            vertex = q.popleft()
            vertexList[vertex] = 1
            for connections in rooms[vertex]:
                if not vertexList[connections]:
                    q.append(connections)

        for x in vertexList:
            if not x:
                return False

        return True