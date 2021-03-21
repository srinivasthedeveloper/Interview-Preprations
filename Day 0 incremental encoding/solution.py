(lambda string:print("".join([chr(ord('A')+(ord(string[i])-ord('A')+i)%26) if(string[i].isupper())else chr(ord('a')+(ord(string[i])-ord('a')+i)%26) for i in range(len(string))])))(input().strip())
'''
#OneLiner Brief
string=input().strip()
for i in range(len(string)):
	if(string[i].isupper()):
		print(chr(ord('A')+(ord(string[i])-ord('A')+i)%26),end="")
	else:
		print(chr(ord('a')+(ord(string[i])-ord('a')+i)%26),end="")
'''