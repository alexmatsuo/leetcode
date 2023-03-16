def reverse(x: int) -> int:
    nreversed = 0
    counter = 0
    original = x
    while x / 10 > 1 :
        x = x/10
        counter += 1
    while original / 10 > 0 :
        nreversed = nreversed + original % 10  * 10 ** counter
        original = original // 10
        counter -= 1
    return nreversed



def isPalindrome(x: int) -> bool:
    if x < 0 :
        return False
    else : 
        rev = reverse(x)
        if rev == x :
            return True
        else :
            return False

result = isPalindrome(1231)
print(result)