def isPalindrome(text):
	return text == text[::-1]

text = input()
check = isPalindrome(text)

if check:
	print("ok")
else:
	print("no ok")
