import re

def reverseParentheses(s):
    lparen, rparen = [],[]
    for i in range(len(s)):
        if s[i] == "(":
            lparen.append(i)
        elif s[i] == ")":
            rparen.append(i)
    print(lparen, rparen)
    # for the first right paren, find the left paren that's closest on its left
    for rindex in rparen:
        
            

reverseParentheses("a((bc)de)")
reverseParentheses("a(bc)(de)")
