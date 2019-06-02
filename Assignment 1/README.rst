Assignment 1
=====

In this assignment you will implement a few Python programs related to cryptography, and answer a few questions related to them.


Task 1: Encryption
-------

* Define the function afencode(text, a, b) in affine.py with three parameters, text, a and b.
* Parameter text is a string to be encrypted.
* Parameters a and b form the key of the cipher.
* The function should process each character in text, if the character is a letter, encrypt it using Affine Cipher, otherwise, the character is retained.
* Once the function is implemented in affine.py, you can test the funtion with the following code in main.py ::

    from affine import *
    text = "Attack!"
    a = 9
    b = 13
    cipher = afencode( text, a, b )
    print( text, "=>", cipher )

which produces the output ::

        Attack! => Nccnfz!

* Note that the letter case is preserved.
* You can assume that the parameter text is always a string, the paramters a and b are always integers.

Task 2: Decryption
-------

* Define the function afdecode(cipher, a, b) in affine.py with three parameters, cipher, a and b.
* Parameter cipher is a string to be decrypted.
* Parameters a and b form the key of the cipher.
* The function should process each character in Cipher, if the character is a letter, decrypt it using Affine Cipher, otherwise, the character is retained.
* Once the function is implemented in affine.py, you can test the funtion with the following code in main.py ::

        from affine import *
        cipher = "Nccnfz!"
        a = 9
        b = 13
        text = afdecode( cipher, a, b )
        print( cipher, "=>", text )

which produces the output ::

        Nccnfz! => Attack!

* Note that the letter case is preserved.
* You can make use of the given mInverse() function to find the inverse of a.
* You can assume that the parameter cipher is always a string, the parameters a and b are always integers, and there is an inverse for parameter a.

Task 1: RSA encryption
-------

* Define the function rsaencrypt(value, n, e) in rsa.py with three parameters, value, n and e.
* Parameter value is a value to be encrypted.
* Parameters n and e form the public key for the RSA encryption.
* The function should encrypt the value using RSA public key (n,e) and return the resulting code.
* Once the function is implemented in rsa.py, you can test the funtion with the following code in main.py ::

        from rsa import *
        value = 100
        n = 30360138080141                                                                  
        e = 5510009                                                                         
        code = rsaencrypt( value, n, e )
        print( value, "=>", code )

which produces the output of ::

        100 => 15251238784560

* You can assume that the parameters value, n, and e are always integers.


Task 2: RSA decryption
-------

* Define the function rsadecrypt(value, n, d) in rsa.py with three parameters, value, n and d.
* Parameter value is a value to be encrypted.
* Parameters n and d form the private key for the RSA decryption.
* The function should decrypt and return the code using RSA private key (n,d) and return the resulting value.
* Once the function is implemented in rsa.py, you can test the funtion with the following code in main.py ::

        from rsa import *
        code = 15251238784560
        n = 30360138080141                                                                  
        d = 24201026397005
        value = rsadecrypt( code, n, d )
        print( code, "=>", value )
        
which produces the output of ::

        15251238784560 => 100

* You can assume that the parameters value, n, and d are always integers.


Task 3: RSA hacking
-------

* Given a public key, e.g., (493, 11), if n can be factorized, it is possible to derive a private key from the public key.
* Define the function rsahack(n, e) in rsa.py with two parameters, n and e.
* Parameter n and e form a public key for RSA encryption.
* The function should try to factorize n and calculate the d that forms the private key.
* Once the function is implemented in rsa.py, you can test the funtion with the following code in main.py ::

        from rsa import *
        n = 493                                                                  
        e = 11
        d = rsahack( n, e )
        print( n, ",", e, "=>", d )
 
which produces the output of ::
 
        493, 11 => 163
 
* It is part of the assignment that you need to find out how the value of d can be calculated.
* You can make use of the mInverse() function provided in the previous question to calculate the multiplicative inverse.
* You can assume that the parameters n, and e are always integers, and n will be small enough to be easily factorized.


