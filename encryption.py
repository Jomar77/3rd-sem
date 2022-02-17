def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
#check the above function
text = "jnynl vxnj ht fvln"

print ("Text  : " + text)
for i in range(27):
    print ("Shift : " + str(i))
    print ("Cipher: " + encrypt(text,i))
