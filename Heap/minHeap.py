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

    def extract(self):
        if not self.arrayList:
            return None
        if len(self.arrayList) == 1:
            return self.arrayList.pop()
        else:
            self.arrayList[0] = self.arrayList.pop()

            i = 0
            left = (2 * i) + 1
            right = left + 1

            while left <= len(self.arrayList):
                if self.arrayList[i] > self.arrayList[left] and self.arrayList[i] > self.arrayList[left]:
                    minChild = min(left, right)
                    self.arrayList[minChild], self.arrayList[i] = self.arrayList[i], self.arrayList[minChild]
                    i = minChild

                    left = (2 * i) + 1
                    right = left + 1
                else:
                    break





h = MinHeap()
h.insert(8)
h.insert(18)
h.insert(10)
h.insert(20)
h.insert(28)
h.insert(39)
h.insert(29)
h.insert(37)
h.insert(26)
h.insert(76)
h.insert(32)
h.insert(74)
h.insert(89)
h.insert(66)
h.extract()
h.extract()
h.extract()


