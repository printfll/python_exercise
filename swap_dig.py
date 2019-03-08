import sys
def swap(digits, n1, n2):
    idx1, idx2 = -1, -1
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == n1 and idx1<0:
            idx1 = i
            if n1==n2:
                continue
        if digits[i] == n2 and idx2<0:
            idx2 = i
    step = abs(len(digits)-2-idx1)+abs(len(digits)-1-idx2)# move from idx1, idx2 to the last two position
    if idx1==0 or idx2==0:# only target digit is at the start, we need to deal with leading zero
        if idx1+idx2==1:#case find "25" in "25001234", "2" and "5" are the beginning 2 digits
            for i in range(2, len(digits)):
                if digits[i]!=0:
                    step += i-2
                    return step
        else:#only one digit is at the start
            for i in range(1, len(digits)):
                if digits[i]!=0 and i!=idx1 and i!=idx2:
                    step += i-1
                    return step
        return sys.maxsize # find "25" in "250", but after swap, "025" is invalid
    return step

def min_swap(digits):
    if len(digits)<2:
        return -1
    if not int(digits[-2:])%25:
        return 0
    steps = []
    if digits.count("0")>=2:
        steps.append(swap(digits, "0", "0"))
    if digits.count("2")>=1 and digits.count("5")>=1:
        steps.append(swap(digits, "2", "5"))
    if digits.count("7")>=1 and digits.count("5")>=1:
        steps.append(swap(digits, "7", "5"))
    if digits.count("0")>=1 and digits.count("5")>=1:
        steps.append(swap(digits, "5", "0"))
    min_step = min(steps) if steps else sys.maxsize
    return min_step if min_step<sys.maxsize else -1
string = "200683239823445"
print(min_swap(string))#3