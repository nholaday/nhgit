def reverseParentheses(s):
    """Looks for the first ) then moves back until it finds (
    then it reverses what's in the the parens and drops them and starts over
    """
    index = 0
    while index < len(s):
        if s[index] == ")":
            s = reverseWord(s,index)
            index = 0
        else:
            index += 1
    return s

def reverseWord(s, i):
    end = i
    # May be able to do this with s.rfind('(',0,i)
    while s[i] != "(":
        i -= 1
    s = s[:i] + s[i+1:end][::-1] + s[end+1:]
    return s
        
if __name__ == "__main__":
    reverseParentheses("a((bc)de)")
    reverseParentheses("a(bc)(de)")
