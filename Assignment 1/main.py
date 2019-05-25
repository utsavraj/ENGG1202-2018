from affine import *

text = str(input("Enter your text = "))
cipher1 = str(input("Enter your cipher = "))
a = int(input("Key a = "))
b = int(input("Key b = "))

cipher = afencode( text, a, b )
text1 = afdecode(cipher1, a, b)
print( text, "=>", cipher)
print( cipher1, "=>", text1)