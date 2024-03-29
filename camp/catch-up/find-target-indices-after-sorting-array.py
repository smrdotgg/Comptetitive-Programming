class Sorter:
    def quickSort(self, arr):
        self.arr = arr
        self.qs(0, len(arr) - 1)
        return self.arr
    
    def qs(self, left, right):
        if left >= right: return

        pivot = self.arr[((right+left)// 2)]
        index = self.partition(pivot, left, right)
        self.qs(left, index-1)
        self.qs(index, right)

    
    def partition(self, pivot, left, right):
        while left <= right:
            while self.arr[left] < pivot: left += 1
            while self.arr[right] > pivot: right -= 1

            if (left <= right):
                (self.arr[left], self.arr[right]) = (self.arr[right], self.arr[left])
                left +=1
                right -=1
        
        return left

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        s = Sorter()
        sortedNums = s.quickSort(nums)
        finalList = []

        finished = False
        for n in range(len(nums)):
            if nums[n] == target:
                finished = True
                finalList.append(n)
            elif(finished): break

        return finalList 
