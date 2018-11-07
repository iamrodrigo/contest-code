def shortestSec(desiredTags, targetList):
    maxIndex = len(targetList)
    minIndex = 0
    desiredTagsSet = set()
    desiredTagsDictionary = {}

    for e in desiredTags:
        desiredTagsSet.add(e)
        desiredTagsDictionary[e] = -1

    for i,e in enumerate(targetList):
        if e in desiredTagsDictionary:
            desiredTagsDictionary[e] = i

            if e in desiredTagsSet:
                desiredTagsSet.remove(e)

            if not len(desiredTagsSet):
                minTagIndex = len(targetList)

                for x in desiredTagsDictionary.values():
                    minTagIndex = min(minTagIndex, x)

                    if i - minTagIndex > maxIndex - minIndex:
                        break

                if i - minTagIndex < maxIndex - minIndex:
                    maxIndex = i
                    minIndex = minTagIndex

    print(minIndex, maxIndex)

shortestSec(['in', 'the', 'spain'], ['the', 'spain', 'that', 'the', 'rain', 'in', 'spain', 'stays', 'forecast', 'in', 'the'])



