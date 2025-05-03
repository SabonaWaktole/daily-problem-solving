# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = defaultdict(int)
        email_to_name = {}
        acc_owner = defaultdict(set)

        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if rank[rx] > rank[ry]:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
                    if rank[rx] == rank[ry]:
                        rank[ry] += 1

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                union(first_email, email)
                email_to_name[email] = name

        for email in email_to_name:
            root = find(email)
            acc_owner[root].add(email)

        result = []
        for root in acc_owner:
            name = email_to_name[root]
            emails = sorted(acc_owner[root])
            result.append([name] + emails)

        return result
