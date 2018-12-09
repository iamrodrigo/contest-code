class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.times = times
        self.winnerAtTime = []
        self.totalVotes = {}

        lastWinner = persons[0]

        for candidate in persons:
            if candidate not in self.totalVotes:
                self.totalVotes[candidate] = 0
            self.totalVotes[candidate] += 1

            self.winnerAtTime.append(candidate if self.totalVotes[candidate] >= self.totalVotes[lastWinner] else lastWinner)
            lastWinner = self.winnerAtTime[-1]

    def q(self, t):
        beginning = 0
        end = len(self.times) - 1
        middle = beginning + ((end - beginning) / 2)

        while beginning < end:
            if self.times[middle] == t or self.times[middle] < t and self.times[middle + 1] > t:
                return self.winnerAtTime[middle]
            else:
                if self.times[middle] > t:
                    end = middle - 1
                else:
                    beginning = middle + 1
            middle = beginning + ((end - beginning) / 2)
        return self.winnerAtTime[middle]