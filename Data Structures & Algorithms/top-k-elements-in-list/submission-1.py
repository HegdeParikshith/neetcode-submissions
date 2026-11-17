class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        
        heap = []
        for i in hashmap.keys():
            heapq.heappush(heap,(hashmap[i],i))
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        