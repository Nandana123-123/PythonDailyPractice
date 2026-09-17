class Solution:
    def isValid(self, s):
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            elif not stack or stack.pop() != ch:
                return False

        return len(stack) == 0


# Main program
s = input("Enter parentheses: ")

obj = Solution()

result = obj.isValid(s)

print(result)