class Solution(object):
    def numUniqueEmails(self, emails):
        totalEmails = set()

        for email in emails:
            atFlag = False
            addFlag = False
            finalEmail = ''
            for c in email:
                if atFlag or c.isalpha() and not addFlag:
                    finalEmail += c
                elif c == '@':
                    finalEmail += c
                    atFlag = True
                elif c == '+':
                    addFlag = True

            if finalEmail not in totalEmails:
                totalEmails.add(finalEmail)

        return len(totalEmails)

s = Solution()
s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])