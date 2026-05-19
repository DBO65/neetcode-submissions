class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        char_s = []

        for c in tokens:
            sol = 0 
            if c == "+":
                sol += int(char_s[-1])
                char_s.pop()
                sol += int(char_s[-1])
                char_s.pop()
                char_s.append(sol)

            elif c == "-":
                sol -= int(char_s[-1])
                char_s.pop()
                sol += int(char_s[-1])
                char_s.pop()
                char_s.append(sol)

            elif c == "/":
                div = int(char_s[-1])
                char_s.pop()
                numer = int(char_s[-1])
                char_s.pop()
                char_s.append(numer/div) 

            elif c == "*":
                factor = int(char_s[-1])
                char_s.pop()
                factor *= int(char_s[-1])
                char_s.pop()
                char_s.append(factor)
            
            else:
                char_s.append(c)

        return int(char_s[0])
        
        
        