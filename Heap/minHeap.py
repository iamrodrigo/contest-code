class MinHeap(object):
    def __init__(self):
        self.arrayList = []

    def insert(self, n):
        self.arrayList.append(n)
        actualPosition = len(self.arrayList) - 1
        parent = (actualPosition - 1) / 2

        while actualPosition > 0 and self.arrayList[parent] > self.arrayList[actualPosition]:
            self.arrayList[parent], self.arrayList[actualPosition] = self.arrayList[actualPosition], self.arrayList[parent]
            actualPosition = parent
            parent = (actualPosition - 1) / 2



h = MinHeap()
h.insert(3)
h.insert(2)
h.insert(1)


