def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1('Python'))
print(any_lowercase1('python'))
#The return is False, since it can only test the first letter for lowercase or uppercase;
#the return stops the evaluation after first letter
# so the function should be wrong because it only checks part of it

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print(any_lowercase2('Python'))
print(any_lowercase2('python'))
#The return for both are True, since it only test the "c" as a string
#It does not check any letters in from the given strings
#so the function should be wrong because it does not check anything

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
print(any_lowercase3('PythoN'))
print(any_lowercase3('pytHon'))
#The return for the first one is False, and the second one is True
#since it can only check the last letter of the given strings
#so the function should be wrong because it only check the last letter

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
print(any_lowercase4('PythoN'))
print(any_lowercase4('pytHon'))
#The reurn for both are True, since both strings contain lowercase
#The function first sets flag as False as default, and when it comes across lowercase letter, the c.islower() becomes True
# String "flag"  becomes False or True which is always True 
#so the function should be correct 

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
print(any_lowercase5('PythoN'))
print(any_lowercase5('python'))
#The return for the first one is False, the second one is True
#It tests if the whole string is lowercase or not
#The first one since it is not all lowercase, so it comes to False; the second one works the opposite
#so the function should be wrong


def rotate_word(rotate,shift):
    rotate_word= ''
    for c in rotate:
        rotate_word += chr(ord(c) + shift)
    return rotate_word    
print(rotate_word('cheer', 7))
print(rotate_word('IBM', -1))





#print(ord('a'))
#print(ord('c')-ord('a'))
#print(chr(ord('a')+2))
#print(chr(ord('y')+2))


message= "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


original_text= ""
for c in message:
    if c >= 'a' and c <= 'z':
        original_text += chr(ord(c)+ 2)
    else:
        original_text += c
print(original_text)

message= "map"


original_text= ""
for c in message:
    if c >= 'a' and c <= 'z':
        original_text += chr(ord(c)+ 2)
    else:
        original_text += c
print(original_text)



