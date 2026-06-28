class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i<j:
            print(i, j)
            add = numbers[j] + numbers[i]
            print(add)
            if add > target:
                j-=1
            elif add < target:
                i+=1
            else:
                return [i+1, j+1]
        return []