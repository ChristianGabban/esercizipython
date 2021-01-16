file1=open("d:/crypto/t.txt","r").read()
print(len(file1))


while True:
        prova = input("cosa vuoi fare?     (1 = codifica | 2 = decodifica | 3 = esci): " )
        if (prova=='1'):
            codifica=input("inserisci la frase da codificare: ")
            while ((len(codifica) <= 0) and (len(codifica)<=len(file1))):
                 if (len(codifica) <= 0):
                    print('codifica impossibile, inserire una frase o parola  ')
                    codifica=input("inserisci la frase da codificare: ")           
            print('frase codificata')
            print('scrittura della frase all interno del file ==>" nomefile.txt"')               
        if (prova=='2'):
            print('decodifica')
        if (prova=='3'):
            exit()
        
