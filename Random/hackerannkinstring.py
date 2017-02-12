import sys
from collections import deque

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    word = deque(['k','n','a','r','r','e','k','c','a','h'])
    for i in range(0,len(s)):
        temp_char = s[i]
        poped_char = word.pop()
        if(not(poped_char is temp_char)):
            word.append(poped_char)
    if(word):
        print("NO")
    else:
        print("YES")