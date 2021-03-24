
"""
51 minutes

Approach:
Use DFS to solve this question.
1. Recursion run for each digit in the input digits
2. At each recursion level, loop thru every letter that are represented by the current level digit
3. In each loop, the program will append the letter to the output string, recursion to next level, and recover the string status

Data structure: a hash table to store numbers, and letters that the number could represent
"""


def letterCombo(digits):
    if len(digits)==0: return [] #empty string check
    letters={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

    def helper(level,digits,temp):
        #base case
        if level==len(digits):
            output.append(''.join(temp)) #add string to final result
            return
        #recursive rule
        dlist=list(letters[digits[level]])
        for i in range(0,len(dlist)): #loop thru each letter in the number-letter list in the hashtable
            temp.append(dlist[i]) #append letter to string
            helper(level+1,digits,temp) #recursion to next level
            temp.pop() #recover status

    temp,output,level=[],[],0
    helper(level,digits,temp)

    return output



"""Test Cases"""
#digits=""
#digits="2"
digits="23"
#digits="237"
print("Output: ", letterCombo(digits))


"""
Time Complexity: O(M^N) or O(4^N). M is the maximum number of letters represented by a single digit in the input digits. N is the length of the input digit.
                The recursion will go N level. At each level, the loop will loop every letter that are represented by the digit in the input digits.
                In this case, the maximum number of letters represented by a single digits is 4 ("7" and "9"), so M=4, and the time complexity is O(4^N).

Space Complexity: O(N). N is the length of the input digits.
                The program only needs to use a temporary list in the recursion to store N digits.

"""
