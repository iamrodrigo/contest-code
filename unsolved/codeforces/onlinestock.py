class Node(object):
    def __init__(self, pos = 0, price = 0, biggest = None):
        self.pos = pos
        self.price = price
        self.biggest = biggest

class StockSpanner(object):

    def __init__(self):
        self.latest = None
        self.biggest = None
        self.first = None

    def next(self, price):
        if self.latest == None:
            self.latest = Node(1, price)
            self.first = self.biggest = self.latest
            return 1
        elif self.biggest.price < price:
            self.biggest = self.latest = Node(self.latest.pos+1, price, self.first)
            return self.latest.pos
        else:
            count = 0
            node = self.latest
            while node != None:
                count += 1
                if price < node.price:
                    self.latest = Node(self.latest.pos+1, price, node)
                    return count
                else:
                    count += abs(node.pos - (node.biggest.pos if node.biggest else 0)) - 1
                    node = node.biggest

            self.biggest = self.latest = Node(self.latest.pos + 1, price, self.first)
            return self.latest.pos

S = StockSpanner()
print S.next(10)# is called and returns 1,
print S.next(9)# is called and returns 1,
print S.next(8)# is called and returns 1,
print S.next(7)#is called and returns 2,
print S.next(6)# is called and returns 1,
print S.next(7)
print S.next(8)
print S.next(8)
print S.next(8)
print S.next(9)
print S.next(10)
