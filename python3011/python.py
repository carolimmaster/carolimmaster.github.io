def affiche (anneau:int, départ:int, arrivee:int):->None
	print("on déplace l'anneau anneau "du piquet départ "au piquet",arrivee)
	
def piquet_en_plus(depart: int, arrivee:int):->int:
	return 6-depart arrivee
	

def hanoi (anneaux :int,depart:int, arrivee:int)->int:
	if anneaux==1
		affiche (1,depart,arrivee)
		return 1
	else
	a=hanoi (anneaux-1,depart piquet_en_plus (depart arrivee))
	affiche (anneaux depart arrivee)
	b=hanoi (anneaux-1,piquet_en_plus(depart,arrivee)arrivee)
	return a+b+1