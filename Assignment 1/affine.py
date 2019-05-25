def afencode(text, a, b):
    str=""
    if b in range (25) and a in range (25):
        sum = 0
        for ch in text:
            if ord(text[sum]) >= ord( 'a' ) and ord(text[sum]) <= ord( 'z' ):
                ord_alphabet = ord(text[sum]) - ord('a')
                n = ((a*(ord_alphabet)) + b)%26
                d = n + ord('a')
                str+=chr(d)
                #print (chr(d), end="") #return doesn't work because stops
                sum += 1

            
            elif ord(text[sum]) >= ord( 'A' ) and ord(text[sum]) <= ord( 'Z' ):
                ord_alphabet = ord(text[sum]) - ord('A')
                n = ((a*(ord_alphabet)) + b)%26
                d = n + ord('A')
                str+=chr(d)
                #print (chr(d) , end="")
                sum += 1
                
            else:
                str+=text[sum]
                #print (text[sum] , end="")
                sum +=1
        return str
                
    else:
        print("ERROR: Choose correct value for b/a")
        
#--- decryption ----#
def mInverse( a, y ):
    r0, r1, t0, t1 = y, a, 0, 1
    while r1 > 1:
        q = r0 // r1
        r2 = r0 - r1 * q
        t2 = t0 - t1 * q
        r0, r1 = r1, r2
        t0, t1 = t1, t2
 
    if r1 == 1:
        return t1 % y
    return print("Choose another value for a") 

def afdecode(cipher1, a, b):
    str1=""
    if b in range (25) and a in range (25):
        y = 26
        sum = 0
        for ch in cipher1:
            if ord(cipher1[sum]) >= ord( 'a' ) and ord(cipher1[sum]) <= ord( 'z' ):
                ord_alphabet = ord(cipher1[sum]) - ord('a')
                n = ((mInverse( a, y ))*((ord_alphabet) - b))%26
                d = n + ord('a')
                str1+=chr(d)
                #print (chr(d), end="") #return doesn't work because stops
                sum += 1

            
            elif ord(cipher1[sum]) >= ord( 'A' ) and ord(cipher1[sum]) <= ord( 'Z' ):
                ord_alphabet = ord(cipher1[sum]) - ord('A')
                n = ((mInverse( a, y))*((ord_alphabet) - b))%26
                d = n + ord('A')
                str1+=chr(d)
                #print (chr(d) , end="")
                sum += 1
                
            else:
                str1+=cipher1[sum]
                #print (cipher1[sum] , end="")
                sum +=1
        return str1    
                
    else:
        print("ERROR: Choose correct value for b/a")
        

