class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        index = k
        k = tickets[k]
        total = 0

        if (index < len(tickets)-1):
            total += index + 1
            for i in range(index+1):
                curr = tickets.pop(0)
                tickets.append(curr-1)
        k = tickets[-1]
        for i in range(len(tickets)):
            total += min(tickets[i], k)
        
        return total


