class MagicDictionary(object):

    def __init__(self):
        self.head = {}

    def buildDict(self, dict):
        for w in dict:
            node = self.head

            l = len(w)
            if not l in self.head:
                node[l] = {}

            node = node[l]

            for c in w:
                if not c in node:
                    node[c] = {}

                node = node[c]

            node['*'] = None

    def find(self, word, index, node, errors):
        if errors > 1 or '*' in node:
            return errors

        for key, value in node.iteritems():
            errors = errors if word[index] == key else errors + 1
            errors = self.find(word, index + 1, value, errors)

        return errors

    def search(self, word):
        node = self.head

        if len(word) not in node:
            return False

        errors = self.find(word, 0, node[len(word)], 0)
        return errors == 1

# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
dict = ["hello","hallo","leetcode"]
obj.buildDict(dict)
print obj.search('hello')
print obj.search('hhllo')
print obj.search('hell')
print obj.search('leetcoded')