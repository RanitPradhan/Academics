s = input()
print(any(map(str.isalnum,s)))
print(any(map(str.isalpha,s)))
print(any(map(str.isdigit,s)))
print(any(map(str.islower,s)))
print(any(map(str.isupper,s)))

# Another method

'''
s = input()
one = False
two = False
three = False
four = False
five = False

for i in s:
    if not one:
        one = i.isalnum()
    if not two:
        two = i.isalpha()
    if not three:
        three = i.isdigit()
    if not four:
        four = i.islower()
    if not five:
        five = i.isupper()
print(one)
print(two)
print(three)
print(four)
print(five)
'''