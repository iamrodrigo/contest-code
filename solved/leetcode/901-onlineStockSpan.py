class StockSpanner(object):

    def __init__(self):
        self.q = []

    def next(self, price):

        spanStock = 0
        while len(self.q) and self.q[-1][0] < price:
            spanStock += self.q.pop()[1]

        self.q.append((price, spanStock + 1))
        return self.q[-1][1]


S = StockSpanner()
print S.next(100)# is called and returns 1,
print S.next(80)# is called and returns 1,
print S.next(60)# is called and returns 1,
print S.next(70)#is called and returns 2,
print S.next(60)# is called and returns 1,
print S.next(75)
print S.next(85)
#print S.next(8)
#print S.next(8)
#print S.next(9)
#print S.next(10)
