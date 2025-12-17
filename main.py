#LeetCode problems

class Solution:


######################################### EASY#############################################

# Sum of 2 elements in Array

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [i, map[complement]]
            else:
                map[nums[i]] = i

# Palindrome Int

    def isPalindrome(self, x: int) -> bool:

        if x<0 or (x%10 == 0 and x !=0):
            return False

        reverse = 0
        while x>reverse:
            reverse = reverse *10 + x%10
            x = x//10
        return reverse == x or x ==reverse // 10

# Roman to Int

    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        total = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                total -=roman[s[i]]
            else:
                total += roman[s[i]]
        return total
    
# Int to Roman

    def intToRoman(self, num: int) -> str:
            roman_dict = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
            #2074
            roman_str = []
            for key,val in roman_dict.items():
                while num >= int(key):
                    roman_str.append(val)
                    num -= int(key)
            return "".join(roman_str)

# Longest Common Prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for str in strs:
            while not str.startswith(prefix):
                prefix = prefix[:-1]
                continue
        return prefix
    
#Valid Paranthesis

    def isValid(self, s: str) -> bool:
        mapping ={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for ch in s:
            if ch in mapping:
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack

####################################### MEDIUM ############################################

# Smooth descending periods problem
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 1
        streak = 1
        for i in range(1,len(prices)):
            if prices[i] == prices[i-1]-1:
                streak +=1
            else:
                streak = 1
            result +=streak 
        return result

#Remove sub folders
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        list = [folder[0]]
        for k in range(1,len(folder)):
            prefix = list[-1]+"/"
            if not folder[k].startswith(prefix):
                list.append(folder[k])
        return list

#Fancy String problem
    def makeFancyString(self, s: str) -> str:
        result =[s[0]]
        count = 1

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count +=1
            else:
                count = 1
            if count <=2:
                result.append(s[i])

            # if len(s) < 3:
            #     return s
    
            # temp = ''
            # for a,b,c in zip(s," "+s,"  "+s):
            #     if a == b == c:
            #         continue
            #     temp += a
 
        return "".join(result)

#Largest unique sub array(Sliding Window)

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen_elements = set()
        left = 0
        sum = 0
        max_sum = 0
        for right in range(len(nums)):
            
            while nums[right] in seen_elements:
                seen_elements.remove(nums[left])
                sum -= nums[left]
                left += 1
            
            seen_elements.add(nums[right])
            sum +=nums[right]
            max_sum = max(max_sum,sum) 
            
            
        return max_sum

# Maximum Score From Removing Substrings
    def remove_pattern(self,s,first,second,points):
        stack = []
        score = 0
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                score +=points
            else:
                stack.append(ch)
        return score,"".join(stack)

    def maximumGain(self, s: str, x: int, y: int) -> int:
        total = 0
        if x>y:
            score,s = self.remove_pattern(s,'a','b',x) 
            total +=score
            score,s = self.remove_pattern(s,'b','a',y) 
            total +=score
        else:
            score,s = self.remove_pattern(s,'b','a',y) 
            total +=score
            score,s = self.remove_pattern(s,'a','b',x) 
            total +=score
        return total

# Hills-Valleys count
            
    def countHillValley(self, nums: List[int]) -> int:
        formatted_list = [nums[0]]
        hills_count = 0
        valleys_count = 0
        total_count = 0
        for i in range(1, len(nums)):
            if not nums[i] == nums[i-1]:
                formatted_list.append(nums[i])
        for i in range(1, len(formatted_list)-1):
            if formatted_list[i-1]<formatted_list[i]>formatted_list[i+1]:
                hills_count +=1
                total_count +=1
            if formatted_list[i-1]>formatted_list[i]<formatted_list[i+1]:
                valleys_count +=1
                total_count +=1
        return total_count

solution = Solution()
#result = solution.getDescentPeriods([3,2,1,4])
#result = solution.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
#result = solution.makeFancyString('Helllo Neeel')
#result = solution.makeFancyString([5,2,1,2,5,2,1,2,5])
#result = solution.maximumGain("cdbcbbaaabab",4,5)
print(f"result: {result}")
