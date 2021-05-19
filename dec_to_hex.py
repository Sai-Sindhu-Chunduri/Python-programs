#Hex --> 16 --> 0 to 9 --> A B C D E F
'''10-->A
   11-->B
   12-->C
   13-->D
   14-->E
   15-->F
input-->dec=2545%16
dec_val=""
Step1-->n%16-->rem=1
        if rem<=9
        dec_val+=chr(48+rem)
        else:
        dec_val+=chr(55+rem)
'''

#Program to  change decimal to hexadecimal.
n=2545
hex_val=""
while n:
    rem=n%16
    if rem<=9:
        hex_val+=chr(48+rem)
    else:
        hex_val+=chr(55+rem)
    n=n//16
print(hex_val[::-1])
