

def pallindrome(str):
   
   clean_str = (str.replace(" ", "")).lower()
   reverse_str = clean_str[::-1]
   return clean_str==reverse_str


text=(input("Enter string: "))
if(pallindrome(text)):
   print("Yes") 
else:
   print("No")

