import string


def encrypt(text, key):
    text = text.lower()
    key = key.lower()
    codificato = ""
    abc=string.ascii_lowercase
    for i,c in enumerate(text):
        a=abc.index(c)
        b = abc.index(key[i])
        c=chr((a+b) % 26+97)
        codificato += c
    return codificato

def decrypt(codificato,key):
    key = key.lower()
    codificato = codificato.lower()
    abc = string.ascii_lowercase
    decodificato = ""
    for i,c in enumerate(codificato):
        a = abc.index(c)
        b = abc.index(key[i])
        c = chr((a-b) % 26 + 97)
        decodificato += c.lower()
    return decodificato

try:
 chiave = open("key.txt","r").read()
except IOError as e:
 raise ('Error: can not write ' + chiave + ': ' + str(e))


while True:
        prova = input("cosa vuoi fare?     (1 = codifica | 2 = decodifica | 0 = esci): " )
        if (prova == '1'):
            codifica = input("inserisci la frase da codificare: ")
            while ((len(codifica) == 0) or (len(codifica) > len(chiave))):
                print('la parola inserita è più  lunga della chiave,  per favore inserire un altra frase o parola  ')
                codifica=input("inserisci la frase da codificare: ")  
            codificata=encrypt(codifica,chiave)
            filecodifica=open("ciphertext.txt","w")
            filecodifica.write(codificata)
            filecodifica.close()                
            print('frase codificata:' + codificata)   
        if (prova == '2'):
            codificato = open("ciphertext.txt","r").read()
            decodificato = decrypt(codificato,chiave)
            print('file decodifica: ' + decodificato )
        if (prova =='0'):
            exit()
        
