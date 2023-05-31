class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        
        for i in reversed(range(len(digits))):
            if digits[i] + plus <= 9:
                digits[i] += 1
                
                return digits
            else:
                digits[i] = 0
            
        digits.insert(0, 1)
        
        return digits
            