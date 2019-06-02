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

