# Encrypt Vigenere Cipher Messages

# Encrypting the message using the Vigenere ciphering process
def va_decrypt(strn, k):
    st = ""
    for i in range(len(strn)):
        s = ((ord(strn[i]) - ord(k[i]) +26) % 26) + ord('A')
        st += chr(s)
    return st

# Key function to make the key of the length of message
def key(l):
    t = input("Enter key : ")
    s = t
    i = 0
    while len(s) != l:
        s += chr(((ord(st[i]) - ord(s[i])) % 26) + ord('A'))
        i += 1
    return s

# Execution of the whole Encoding Process
t = ""
while t != "exit":

    print("Enter message to encrypt")
    st = input()
    k = key(len(st))
    print(k)
    e_msg = va_decrypt(st, k)
    print(e_msg)

    print("Want to encrypt again? Press 'c'. Or Press 'exit' to end process.")
    t = input()
