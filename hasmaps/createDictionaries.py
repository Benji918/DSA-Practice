class Solution:
    def sumFourDivisors(self, nums) -> int:
        for num in nums:
            divs = self.FindDivisors(num)

            if len(divs) == 4:
                return sum(divs)

        return 0
        
    def FindDivisors(self, num):
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        
        return divisors
    

fourdivs = Solution()

list_of_numbers = [21,21]

result = fourdivs.sumFourDivisors(nums=list_of_numbers)

        