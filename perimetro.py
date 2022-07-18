def perimetro():	#il def è un comando che permette di realizzare funzioni costituite da diverse istruzioni.
	print("Il programma calcola il perimetro di una figura geometrica")	#scopo del programma
	print("""
	- Quadrato >>1
	- Rettangolo >>2
	- Cerchio >>3
	- Triangolo >>4""")	#opzioni disponibili per l'utente

	print("Inserisci la scelta")
	scelta=int(input(">>> "))	#inserimento dell'opzione scelta dall'utente
	if scelta == 1:		#da qui iniziano la realizzazione delle istruzioni delle scelte
        	print("Hai selezionato il perimetro del quadrato")
        	lato_1 = float(input("Inserisci il valore del lato del quadrato: "))
        	print("Il valore del perimetro del quadrato, avente lato", lato_1, "è :", lato_1*4)
	elif scelta == 2:
        	print("Hai selezionato il perimetro del rettangolo")
        	base = float(input("Inserisci il valore della base: "))
        	altezza = float(input("Inserisci il valore dell'altezza: "))
        	print("Il valore del rettangolo avente base ", base, "e altezza ",altezza, "è :", (base + altezza)*2)
	elif scelta == 3:
        	print("Hai scelto il perimetro dl cerchio")
        	diametro = float(input("Inserisci il diametro del cerchio: "))
        	print("Il valore del perimetro avente diametro ", diametro, "è: ", 3.14 * diametro)
	elif scelta == 4:
		print("Hai scelto il perimetro del triangolo equilatero")
		lato_2 = float(input("Inserisci il lato del triangolo equilatero: "))
		print("Il valore del triangolo equilatero avente lato ", lato_2, "è: ", lato_2*3)
	else:		#in caso venga inserito un numero differente da quelli dati a dispozione, il programma restituirà questo messaggio
        	print("Inserisci una scelta valida")
perimetro()	#qui viene richiamata la funzione per poterla utilizzare
