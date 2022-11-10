class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalCard = len(cardPoints)
        middle = totalCard - k
        Total = sum(cardPoints)
        sumMiddle = temp = sum(cardPoints[:middle])

        for i in range (k):
            temp -= cardPoints[i]
            temp += cardPoints[i+middle]
            sumMiddle = min(sumMiddle,temp)
        return Total-sumMiddle