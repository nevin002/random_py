
str1=input("enter first word:")

str2=input("enter first word:")
if len(str1)!= len(str2):
    print("not an anagram")
else:
    str1=str1.lower()
    str2=str2.lower()
    if sorted(str1) == sorted(str2):
        print("anagram")