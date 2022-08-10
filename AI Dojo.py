#Question_One
String = input("Enter String : ")
print("-----Original String------")
print(String)
print("-----After_Remove_Character------")
new_string = String.replace('a', '')
print(new_string)



#Question_Two
#Range numbers check
a = int(input("Start Checking : "))
b = int(input("End Checking  : "))

print("Prime numbers between", a, "and", b, "are:")

for x in range(a, b + 1):
   if x > 1:
       for i in range(2, x):
           if (x % i) == 0:
               break
       else:
           print(x)



#Question_Three
def count(s, c) :
    res = 0
    for i in range(len(s)) :
        if (s[i] == c):
            res = res + 1
    return res
str= "AI Dojo"
c = 'o'
print(count(str, c))
