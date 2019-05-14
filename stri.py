import re
c=0
King=input()
for i in King:
  if i.isdigit() or i.isalpha() or re.findall('[r"^@#$%&*)(!"]',i):
    c=c+1
print(c) 
