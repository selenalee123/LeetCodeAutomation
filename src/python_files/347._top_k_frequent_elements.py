
"""
LeetCode Problem: 347. Top K Frequent Elements
LeetCode Link: https://leetcode.com/problems/top-k-frequent-elements/description/

Problem Description:
[Provide a brief description of the problem]

Solution:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        using hasmap 
        test = collections.Counter(nums)
        res = test.most_common(k)
        print(res)
        return [ e[0] for e in res]
       
        # counter = collections.Counter(nums)
        # heapmax = [[-fr, num] for num, fr in counter.items()]
        # heapq.heapify(heapmax)
        # list1 = []
        # for i in range(k):
        #     pop = heapq.heappop(heapmax)
        #     list1.append(pop[1])
        # return list1

        # #         Initial counter:
        # # {3: 2, 1: 3, 4: 1, 2: 2}

        # # Heapmax (negative frequency, number):
        # # [(-3, 1), (-2, 2), (-2, 3), (-1, 4)]

        # # After heapify:
        # #           (-1, 4)
        # #          /        \
        # #   (-2, 2)      (-2, 3)
        # #  /
        # # (-3, 1)

        # # After extracting elements (k = 3):
        # # Step 1: pop = (-1, 4), list1 = [4]
        # # Step 2: pop = (-2, 2), list1 = [4, 2]
        # # Step 3: pop = (-2, 3), list1 = [4, 2, 3]

        # # Return: [4, 2, 3]
            











       

        

"""

# Test cases
# Add test cases to validate your solution
