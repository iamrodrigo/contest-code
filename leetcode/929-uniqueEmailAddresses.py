class Solution(object):
    def numUniqueEmails(self, emails):
        totalEmails = set()

        for email in emails:
            username, domain = email.split('@')

            if '+' in username:
                username = username[:username.index('+')].replace('.', '')

            totalEmails.add(username + '@' + domain)

        return len(totalEmails)

s = Solution()
print s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])