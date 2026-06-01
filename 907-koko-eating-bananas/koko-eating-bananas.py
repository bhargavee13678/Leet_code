class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(k):
            total = 0
            for p in piles:
                total += (p+k-1) //k
            return total <= h 
        
        left, right = 1, max(piles)
        answer = right
        while left<= right:
            mid = (left+right) //2
            if can_finish(mid):
                answer = mid
                right= mid-1
            else:
                left = mid +1
        return answer