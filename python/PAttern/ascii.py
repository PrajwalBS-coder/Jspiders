def simpleCipher(en,k):
    output=""
    for i in range(len(en)):
        if(ord(en[i])-k>=65):
         output+=chr(ord(en[i])-k)
        else:
         val=ord(en[i])-k
         if(val<65):
           output+=chr(91-(65-val))
    return output
print(simpleCipher('BMIN',1))