import json
import random
nome_file="prodotto.json"
while True:
    def menu():
        print("BUONGIORNO CLIENTE/PROGRAMMATORE ECCO LE OPERAZIONI CHE PUOI SVOLGERE:")
        print("0.Exit")
        print("1.Mostra tutti i prodotti")
        print("2.Mostra prodotto a seconda dei luoghi di produzione")
        print("3.Mostra prodotto in base alle categorie")
        print("4.Random")
        print("5.carica prodotto")
    menu()
    scelta=input()
    scelta=int(scelta)
    while True:
        match scelta:
            case 0:
                print("Uscita dal programma")
                break
            case 1:
                with open(nome_file,"r") as file:
                    stringa_json=file.read()
        #print(type(stringa_json))
        #print(stringa_json)
                    oggetto_python=json.loads(stringa_json)
        #print(oggetto_python)
        
                for lista in oggetto_python:
                    print(lista)
                do=input("Cosa vuoi comprare?Inserire valori da 1-10: ")
                
                controllo=False
                for elem in oggetto_python:
                    if elem["Prodotto"]==do:
                        controllo=True
                        if elem["Quantita"] is not None and elem["Quantita"]>0:
                            elem["Quantita"]-=1
                            with open(nome_file,"w") as file:
                                json.dump(oggetto_python,file,indent=4)
                            print("Spesa valida!")
                            break
                        else:
                            print("Il prodotto è stato finito,mi dispiace")
                            break
                if(controllo==False):
                    print("Prodotto non trovato")
                scelta1=input("Vuoi continuare la tua spesa? Si, imposta un valore diverso da 0:")
                #scelta1=int(scelta1)
                if scelta1=='0':
                    break
            case 2:
                while True:
                    stringa=str(input("Puoi scegliere il luogo di produzione dei prodotti:Carpenedolo,Milano,Brescia,Castiglione:")).lower()
                    with open(nome_file,"r") as file:
                        stringa_json=file.read()
                        oggetto_python=json.loads(stringa_json)
                        prod=[]
                        for elem in oggetto_python:
                            if elem["Made in"]==stringa:
                                prod.append(elem)
                        if not prod:
                            print("Luogo di produzione non esistente")
                        else:
                            for elementi in prod:
                                print(elementi)
                            do=(input("Cosa vuoi comprare?Inserire valori esposti: "))
                            trovato=False
                            for elem in prod:
                                if elem["Prodotto"]==do:
                                    trovato=True
                                    if elem["Quantita"] is not None and elem["Quantita"]>0:
                                        elem["Quantita"]-=1
                                        for item in oggetto_python:
                                            if item["Prodotto"] == do:
                                                item["Quantita"] = elem["Quantita"]
                                            with open(nome_file,"w") as file:
                                                json.dump(oggetto_python,file,indent=4)
                                        print("Spesa valida!")
                                    else:
                                        print("Il prodotto è stato finito,mi dispiace")
                            if not trovato:
                                print("Prodotto non trovato ")
                    scelta1=input("Vuoi continuare la tua spesa? Si, imposta un valore diverso da 0:")
                    #scelta1=int(scelta1)
                    if scelta1=='0':
                        break
                break
            case 3:
                while True:
                    stringa=str(input("Vedi prodotto in base alla sua categoria->studio,abbigliamento e tecnologico:")).lower()
                    with open(nome_file,"r") as file:
                        stringa_json=file.read()
                        oggetto_python=json.loads(stringa_json)
                        prod=[]
                        for elem in oggetto_python:
                            if elem["Tipologia"]==stringa:
                                prod.append(elem)
                        if not prod:
                            print("Categoria non esistente")
                        else:
                            for elementi in prod:
                                print(elementi)
                            do=(input("Cosa vuoi comprare?Inserire valori esposti: "))
                            trovato=False
                            for elem in prod:
                                if elem["Prodotto"]==do:
                                    trovato=True
                                    if elem["Quantita"] is not None and elem["Quantita"]>0:
                                        elem["Quantita"]-=1
                                        for item in oggetto_python:
                                            if item["Prodotto"] == do:
                                                item["Quantita"] = elem["Quantita"]
                                            with open(nome_file,"w") as file:
                                                json.dump(oggetto_python,file,indent=4)
                                        print("Spesa valida!")
                                    else:
                                        print("Il prodotto è stato finito,mi dispiace")
                            if not trovato:
                                print("Prodotto non trovato ")
                    scelta1=input("Vuoi continuare la tua spesa? Si, imposta un valore diverso da 0:")
                    #scelta1=int(scelta1)
                    if scelta1=='0':
                        break
                break
            case 4:
                while True:
                    with open(nome_file,"r") as file:
                        stringa_json=file.read()
                        oggetto_python = json.loads(stringa_json)
                        codiceErrore=True
                        codiceErrore1=False
                        while True:
                            scelta=input("Vuoi Random o scelta individuale?\n-random\n-individuale\n")
                            if(scelta.lower()=="random"):
                                nScelto = random.randint(1, 10)
                                nScelto=str(nScelto)
                                print(f"il numero prodotto a random={nScelto}\n")
                                break
                                
                            if(scelta.lower()=="individuale"):
                                    nScelto = int(input("Scegli un numero a caso da 1 a 10 per godere un regalo!!!:"))
                                    if 1 <= nScelto <= 10:
                                        nScelto=str(nScelto)
                                        break
                                    else:
                                        print(f"hai inserito {nScelto} che non è tra 1 e 10 TWT")
                            else:
                                print(f"hai inserito {scelta} che non è tra le scelte")
                        
                        
                        for elem in oggetto_python:
                            #for chiave, valore in elem.items():
                            if (elem["Prodotto"] == nScelto and elem["Quantita"] is not None and elem["Quantita"]!=0) :
                                    print(f"Ottimo!!! il prodotto a sorpresa che hai pescato è:{elem["Nome"]}!!!")
                                    codiceErrore1=True
                                    while True:
                                            print("vuoi vedere le carratteristiche di questo prodotto?\nno\nsi")
                                            risposta=input()
                                            if risposta.lower()=="si":
                                                print(elem)
                                                break
                                            if risposta.lower()=="no":
                                                break
                                            else:
                                                print(f"hai inserito {risposta} che non è si o no TWT")
                                    break
                            
                        if codiceErrore1==False:
                                    print("Il prodotto è esaurito TWT")
                                    codiceErrore=False
                                    break   
                                
                                
                        if codiceErrore==True:
                            for elem in oggetto_python:
                                if elem["Prodotto"]==nScelto:
                                        elem["Quantita"]-=1
                            with open(nome_file,"w") as file:
                                json.dump(oggetto_python, file, indent=2)
                        while True:
                            newbuy=(input("Vuoi prendere un'altro regalo?\nsi\nno\n"))
                            if newbuy.lower()=="no":
                                break
                            if newbuy.lower()=="si":
                                break
                            else:
                                print("risposta non valida")
                        if newbuy.lower()=="no":
                            break
                        if newbuy.lower()=="si":
                            print("new cycle")
                break
            case 5:
                carica="prodottoCarica.json"
                with open(carica,"r") as file:
                    caricaJson=file.read()
                    caricaPython = json.loads(caricaJson)
                with open(nome_file,"w") as file:
                    json.dump(caricaPython, file, indent=4)
                break
            case _:
                print("Scelta non valida")
                break
    while True:
        newbuy=(input("Vuoi continuare la spesa?\nsi\nno\n"))
        if newbuy.lower()=="no":
            break
        if newbuy.lower()=="si":
            break
        else:
            print("risposta non valida")
    if newbuy.lower()=="no":
        break
    if newbuy.lower()=="si":
        print("new cycle")
print("Prova")