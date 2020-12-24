str = input()

strlen = len(str)

def palindrome(s):
	slen = len(s)
	
	for i in range(slen // 2):
		if s[i] != s[-(i + 1)] : return False

	return True

flag = True

for k in range(strlen, 0, -1):
	for i in range(strlen - k + 1):
		
		if palindrome(str[i : i + k]) :
			flag = False
			print(k)
			break
	
	if not flag : break