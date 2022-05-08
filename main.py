

def ceaser_encrypt(plaintext: str, key: int) -> str:
    cipher = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        if (ord(char) > 64 and ord(char) < 91):
            cipher += chr((ord(char) + key - 65) % 26 + 65)
        elif ord(char) == 32:
            cipher += char

    return cipher


def main():

    en_freq = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
    [8.16, 1.49, 2.78, 4.25, 12.7, 2.22, 2.01,6.09,6.96,0.15,0.77,4.02,2.40,6.74,7.50,1.92,0.09,5.98,6.32,9.05,2.75,0.97,2.36,0.15,1.97,0.07]]

    pt_freq = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
    [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30,1.28,6.18,0.40,0.02,2.78,4.74,5.05,10.73,2.52,1.20,6.53,7.81,
    4.34,4.63,1.67,0.01,0.21,0.01,0.47]]


    #with open('plaintext.txt', 'r') as f:
    #    file_data = f.read()
    #    f.close()
    
    #ptext = file_data.upper()

    msg = 'HQKQWTFLCGETRTEGROYOEGXQDTFLQUTDLTEKTZQ'
    tab_msg = [[],[]]
    
    for i in range(65,91):
        tab_msg[0].append(chr(i))
        tab_msg[1].append(round(msg.count(chr(i))/len(msg)*100,2))
    
    print(tab_msg)
    print(len(msg))

    
    

if __name__=='__main__':
    main()