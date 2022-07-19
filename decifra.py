

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

freqPTBR = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30,1.28,6.18,0.40,0.02,2.78,4.74,5.05,10.73,2.52,1.20,6.53,7.81, 4.34,4.63,1.67,0.01,0.21,0.01,0.47]

freqEN = [8.16, 1.49, 2.78, 4.25, 12.7, 2.22, 2.01,6.09,6.96,0.15,0.77,4.02,2.40,6.74,7.50,1.92,0.09,5.98,6.32,9.05,2.75,0.97,2.36,0.15,1.97,0.07]

emptyFreq = [0 for i in range(26)]

def getChar (message):
    errorFound = 1

    while (errorFound == 1):
        char = input(message)
        if len(char) != 1:
            print("ERROR! Input only a single letter")
            errorFound = 1
        elif (ord(char) < 65) | ((ord(char) > 90) & (ord(char) < 97)) | (ord(char) > 122):
            print("ERROR! Input only a single letter")
            errorFound = 1
        else:
            errorFound = 0

    if (ord(char) > 96) & (ord(char) < 123):
        char = chr(ord(char) - 32)

    return char

def replaceChars (inputString):
    
    identical = 1
    while (identical == 1):
        out = str(input("Change letters? (Y/N): "))
        if(out == 'N' or out == 'n'):
            exit()
        char1 = getChar("Input 1st character to switch: ")
        char2 = getChar("Input 2nd character to switch 1st with: ")
        if char1 != char2:
            identical = 0
        else:
            print("ERROR! 1st and 2nd characters must be different")

    inputString = inputString.replace(char1, "*")
    inputString = inputString.replace(char2, char1)
    inputString = inputString.replace("*", char2)
    
    return inputString


def ceaser_encrypt(plaintext, key):
    cipher = ''
    for i in range(len(plaintext)):
        char = plaintext[i]
        if (ord(char) > 64 and ord(char) < 91):
            cipher += chr((ord(char) + key - 65) % 26 + 65)
        elif ord(char) == 32:
            cipher += char

    return cipher


def cria_tabela(cifra):
    cifra_ft = dict(zip(letras, emptyFreq))
    tam = len(cifra)

    for char in cifra:
        if char == ' ':
            pass
        else:
            cifra_ft[char] += 1
        

    for k, v in cifra_ft.items():
        cifra_ft[k] = round(v/tam*100, 2)
    
    return dict(sorted(cifra_ft.items(), key=lambda item: item[1], reverse=True))


def main():
    # Esolha entre freq ptbr ou en-us
    #letras_freq = dict(zip(letras, freqEN))
    letras_freq = dict(zip(letras, freqPTBR))
    sorted_letras_freq = dict(sorted(letras_freq.items(), key=lambda item: item[1], reverse=True))

    with open('plaintext.txt', 'r') as f:
        file_data = f.read()
        f.close()
    
    ptext = file_data.upper()

    #cifra = ceaser_encrypt(ptext, 4)
    cifra = "HQKQWTFLCGETRTEGROYOEGXQDTFLQUTDLTEKTZQ"
    print("Mensagem encriptada:  " + cifra)
    
    t = cria_tabela(cifra)
    attemp = cifra
    
    key1 = sorted_letras_freq.keys()
    key2 = t.keys()
    relacao = dict(zip(key2,key1))
    
    attemp = attemp.translate(str.maketrans(relacao))
    print()
    print("Mensagem decriptada:  " + attemp)

    attemp2 = attemp
    while(1):
        attemp2 = replaceChars(attemp2)
        print()
        print("Mensagem decriptada:  " + attemp2)
  
   

if __name__=="__main__":
    main()

