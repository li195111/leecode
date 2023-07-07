from collections import Counter

class Solution:
    '''Approach 1: Binary Search + Fixed Size Sliding Window'''

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        l, r = k, n

        def valid(w):
            counter = Counter(answerKey[:w])
            if min(counter['T'], counter['F']) <= k:
                return True
            for i in range(w, n):
                counter[answerKey[w]] += 1
                counter[answerKey[i-w]] -= 1
                if min(counter['T'], counter['F']) <= k:
                    return True
        while l < r:
            mid = (l+r+1) // 2
            is_valid = valid(mid)

            if is_valid:
                l = mid
            else:
                r = mid - 1
        return l

class Solution:
    '''Approach 2: Sliding Window'''

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        max_size = k
        counter = Counter(answerKey[:k])

        l = 0
        for r in range(k, n):
            counter[answerKey[r]] += 1
            while min(counter['T'], counter['F']) > k:
                counter[answerKey[l]] -= 1
                l += 1
            max_size = max(max_size, r - l + 1)
        return max_size

class Solution:
    '''Approach 3: Advanced Sliding Window'''

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        max_size = k
        counter = Counter(answerKey[:k])

        l = 0
        for r in range(k, n):
            counter[answerKey[r]] += 1
            
            minor = min(counter['T'], counter['F'])
            
            if minor <= k:
                max_size += 1
            else:
                counter[answerKey[r - max_size]] -= 1

        return max_size


if __name__ == '__main__':
    print(Solution().maxConsecutiveAnswers('TTFF',2) == 4)
    print(Solution().maxConsecutiveAnswers('TFFT',1) == 3)
    print(Solution().maxConsecutiveAnswers('TTFTTFTT',1) == 5)
    # print(Solution().maxConsecutiveAnswers('ab','.*c') == False)
