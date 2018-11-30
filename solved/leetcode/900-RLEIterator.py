class RLEIterator(object):

    def __init__(self, A):
        self.currentIndex = 1
        self.remaining = A[0]
        self.A = A

    def next(self, n):
        self.remaining -= n
        while self.remaining < 0:
            self.currentIndex += 2
            if self.currentIndex > len(self.A):
                return -1
            self.remaining += self.A[self.currentIndex - 1]
        return self.A[self.currentIndex]