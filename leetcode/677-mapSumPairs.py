class MapSum(object):

    def __init__(self):
        self.head = {'*': {}}
        self.keys = {}

    def insert(self, key, val):
        newVal = val - self.keys.get(key, 0)
        self.keys[key] = val

        node = self.head['*']
        for c in key:
            if not c in node:
                node[c] = {}

            if not 'total' in node:
                node['total'] = 0

            node['total'] += newVal
            node = node[c]

        if not 'total' in node:
            node['total'] = 0

        node['total'] += newVal

    def sum(self, prefix):
        node = self.head['*']

        for c in prefix:
            if not c in node:
                return 0
            node = node[c]

        return node['total']

s = MapSum()
s.insert("aa", 3)
print s.sum("a")
#s.insert("aab", 4)
s.insert("aa", 2)
print s.sum("aa")