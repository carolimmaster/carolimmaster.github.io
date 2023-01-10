# Algorithmique et Programmation — Master Droit & Informatique — UPEC - Semestre 1 
# Caroline LIM 2022
# Licence TATA & TITI

#Exercice 1 

def arrondi_decime(x:float)-> float:
    #Je définis la fonction dan une balise qui s'appelle "arrondi_decime", qui prend en entrée et qui retourne en sortie un chiffre à virgule
    """Calculer l'arrondi au décime supérieur d'un nombre à virgule"""

    resultat:float=0 
    #Je pose la variable résultat type chiffre à virgule, je lui donne pour valeur zéro
    resultat= round (x,1)
    #J'affecte à la variable résultat une valeur pour qu'elle puisse arrondir la valeur x à un chiffre après la virgule 
    return resultat
    #Je veux qu'il retourne le résultat

assert (arrondi_decime(2.444)) == 2.4
assert (arrondi_decime(2.456)) == 2.5
#Je créé deux tests pour appeler la fonction "arrondi_decime" avec le chiffre 2.444 qui doit me renvoyer 2.4 et un second avec le chiffre 2.456 qui doit me renvoyer 2.5


#Exercice 2

def prixkm(d:int)->float:
    #Je définis ma fonction avec une balise qui s'appelle "prixkm", qui prend en entrée un entier et qui retourne en sortie un chiffre à virgule
    """Donner la signature d'une fonction appelée prixkm prenant en entrée une distance et renvoyant le prix d'un trajet RER en seconde classe sur cette seconde distance"""
    
    a:float=0
    #Je pose la variable a qui est un chiffre à virgule et qui a pour valeur zéro
    b:float=0
    #Je pose la variable b qui est un chiffre à virgule et qui a pour valeur zéro
    if d>=1 and d<=16:
    #Je pose la condition, si distance est supérieur ou égal 1 et inférieur ou égal à 16
        a=0.7781
    #a qui vaut 0.7781  
        b=0.1944
    #b qui vaut 0.1944
    elif d>=17 and d<=32:
    #Sinon si distance est supérieur ou égal à 17 et inférieur ou égal à 32 
        a=0.2503
    #a qui vaut 0.2503
        b=0.2165
    #b qui vaut 0.2165
    elif d>=33 and d<=64:
    #Sinon si distance est supérieur ou égal à 33 et inférieur ou égal à 64
        a=2.0706
    #a qui vaut 2.0706
        b=0.1597
    #b qui vaut 0.1597
    elif d>=65 and d<=109:
    #Sinon si distance est supérieur ou égal à 65 et inférieur ou égal à 109
        a=2.8891
    #a qui vaut 2.8891
        b=0.1489
    #b qui vaut 0.1489
    elif d>=110 and d<=149:
    #Sinon si distance est supérieur ou égal à 110 et inférieur ou égal à 149
        a=4.0864
    #a qui vaut 4.0864
        b=0.1425
    #b qui vaut 0.1425
    elif d>=150 and d<=199:
    #Sinon si distance est supérieur ou égal à 150 et inférieur ou égal à 199 
        a=8.0871
    #a qui vaut 8.0871
        b=0.1193
    #b qui vaut 0.1193
    elif d>=200 and d<=300:
    #Sinon si distance est supérieur ou égal à 200 et inférieur ou égal à 300 
        a=7.7577
    #a qui vaut 7.7577
        b=0.1209
    #b qui vaut 0.1209
    elif d>=301 and d<=499:
    #Sinon si distance est supérieur ou égal à 301 et inférieur ou égal à 499
        a=13.6514
    #a qui vaut 13.6514
        b=0.1030
    #b qui vaut 0.1030
    elif d>=500 and d<=799:
    #Sinon si distance est supérieur ou égal à 500 et inférieur ou égal à 799 
        a=18.4449
    #a qui vaut 18.4449
        b=0.0921
    #b qui vaut 0.0921
    else:
    #Sinon
        a=32.2041
    #a qui vaut 32.2041
        b=0.0755
    #b qui vaut 0.0755
    
    total=float=0
    #Je pose la variable total qui est un chiffre à virgule et qui a pour valeur zéro
    total=a+d*b
    #Je pose la fonction a+d*b qui est la formule utilisée à l'énoncé page une
    return arrondi_decime(total)
    #Je veux qu'il retourne la valeur mais arrondie au décimal

assert (prixkm(73)) == 13.80
#Prix km(73) doit retourner 13.80 

#Exercice 3

def prixkm1ere(d:int)->float:
    # Je définis ma fonction dans une balise qui s'appelle "prixkm1ere", qui prend en entrée un entier et qui retourne en sortie un chiffre à virgule
    """Affiche le tarif en première classe qui est obtenu à partir du tarif de seconde classe en le multipliant par 1,5"""
    total:float=0
    #Je pose ma variable total type chiffre à virgule, je lui donne pour valeur zéro
    total= prixkm(d)*1.5
    #J'appelle la fonction prixkm qui est le prix du billet de second classe et je multiplie le prix par 1.5
    return arrondi_decime(total)
    #Retourne la valeur arrondie au décimal
    
assert(prixkm1ere(73))==20.7
#Prixkm1ere(73)doit retourner 20.7

#Exercice 4

def prix_speciaux_max(d:int)->list[float]:
#Je définis ma fonction dans une balise qui s'appelle "prix_speciaux_max" qui prends en entrée un entier et qui retourne en sortie une liste de nombres à virgule 
    """Calculer le maximum autorisé pour les prix intercités de nuit et intercités réservations à réservation obligatoire"""
    list_de_prix_1erclasse_2emeclasse :list[float] = []
    #Je pose ma variable list_de_prix_1erclasse_2emeclasse qui est une liste de nombre à virgule et qui est vide pour le moment
    list_de_prix_1erclasse_2emeclasse.append(arrondi_decime(prixkm1ere(d)*2.1))
    #Je pose ma variable list_de_prix_1erclasse_2emeclasse dont j'ajoute le prix de la 1ere classe arrondie au décimal et qui est multiplié par 2.1 fois  
    list_de_prix_1erclasse_2emeclasse.append(arrondi_decime(prixkm(d)*2.1))
    #Je pose ma variable list_de_prix_1erclasse_2emeclasse dont j'ajoute le prix de la 2eme classe arrondie au décimal et qui est multiplié par 2.1 fois     
    return list_de_prix_1erclasse_2emeclasse
    #Je retourne le prix intercités de nuit et réservation obligatoire 1ere et seconde classe 

assert(prix_speciaux_max(73))==[43.5, 29]
#Je fais une vérification que le prix maximal en première classe est de 43.5 et de seconde classe 29 pour 73kms

#Exercice 5

def distances (depart:str,arrivee:str)->float:
# Je définis ma fonction dans une balise qui s'appelle "distances", qui prend en entrée deux chaines de caractères et qui retourne en sortie un chiffre à virgule
    """Calculer la distance entre deux gares sinon afficher -1 s'il y a une erreur"""
    a:file
    #Je pose ma variable a qui est de type file pour ouvrir le fichier
    l:str
    #Je pose ma variable l type chaine de caractère qui va lire chaque ligne du fichier
    existant:bool=False
    #Ma variable existant est un booléen qui a pour valeur vrai ou faux
    distance_entre_les_deux_gares:float=0
    #Ma variable distance_entre_les_deux_gares est un chiffre à virgule et prend la valeur 0
    a=open("distances.csv",mode="r")
    #Je pose ma variable a qui va ouvrir le fichier distances.csv mais je veux simplement que Python lis le fichier
    l=a.readline()
    #Je veux qu'il lise la première ligne du fichier
    for l in a.readlines():
    #Ma variable va prendre chaque ligne du fichier
        element:list[str]=l.split(",")
        #Ma variable élément est une liste composée de chaine de caractère dont le premier élément est départ, le deuxième élément est arrivée et le troisième, la distance entre départ et arrivée
        gare_de_depart_fichier:str=element[0]
        #Ma variable gare_de_depart_fichier est une chaine de caractère qui contient element 0 soit la ville de départ
        gare_arrivee_fichier:str=element[1]
        #Ma variable gare_arrivee_fichier est une chaine de caractère qui contient element 1 soit la ville d'arrivée
        distance_fichier:str=element[2]
        #Ma variable distance_fichier est une chaine de caractère qui contient element 2 soit la distance entre la ville de départ et la ville d'arrivée
        if depart==gare_de_depart_fichier and arrivee==gare_arrivee_fichier:
        #Si la variable départ passé en paramètre est égale à la gare du départ dans le fichier, et que, ma variable arrivee est égale à la gare du départ dans la fichier
            existant=True
            #Alors ma variable existant passe à true (vrai) 
            distance_entre_les_deux_gares=float(distance_fichier)
            #Ma variable distance_entre_les_deux_gares prend la valeur distance du fichier
            
    if existant==False:
    #Si non existant 
        print("l'une des gares arrivee ou depart n'existe pas")
        #Affiche "l'une des gares arrivee ou depart n'existe pas"
        return -1
        #Retourne -1 
    else:
    #Sinon on est dans le cas où la gare de départ et la gare d'arrivee sont présents dans le fichier    
        print("depart:",depart)
        #Affiche depart avec la ville de depart
        print ("arrivee:",arrivee)
        #Affiche arrivee avec la ville d'arrivee
        distance_entre_les_deux_gares_en_km:float=distance_entre_les_deux_gares/1000
        #La variable distance_entre_les_deux_gares_en_km égale distance_entre_les_deux_gares divisé par 1000 du fait qu'on passe de kilomètre en mètre 
        distance_km_arrondie_en_entier:int=round(distance_entre_les_deux_gares_en_km)
        #La varialbe distance_km_arrondie_en_entier est un chiffre entier qui est arrondie à l'entier
        print ("distance en mètre:", distance_entre_les_deux_gares)
        #Affiche distance en mètre qui est la distance entre les deux gares 
        print ("distance en km non arrondie:", distance_entre_les_deux_gares_en_km)
        #Affiche distance_entre_les_deux_gares_en_km qui est la distance entre les deux gares en km
        print ("distance en km arrondie:", distance_km_arrondie_en_entier)
        #Affiche distance_km_arrondie_en_entier qui est la distance au kilomètre arrondie en entier
        print("prix_premiere_classe:",prixkm1ere(distance_km_arrondie_en_entier))
        #Affiche le prix de la première classe 
        print("prix_seconde_classe:",prixkm(distance_km_arrondie_en_entier))
        #Affiche le prix de la seconde classe
        print("tarif_particulier 1ère classe :",prix_speciaux_max(distance_km_arrondie_en_entier)[0])
        #Affiche le tarif intercités de nuit et intercités à réservation obligatoire prix max pour 1ere classe 
        print("tarif_particulier 2ème classe :",prix_speciaux_max(distance_km_arrondie_en_entier)[1])
        #Affiche le tarif intercités de nuit et intercités à réservation obligatoire prix max pour 2eme classe 
        return distance_entre_les_deux_gares

print("Test 1 : distance entre Tours et Saint-Pierre-des-Corps")
#Affiche test 1 qui émet la distance entre Tours et Saint-Pierre-des-Corps
assert(distances("Tours","Saint-Pierre-des-Corps"))==2711.674
#Je fais une vérification que la distance entre la gare de Tours (gare de départ), et la gare Saint-Pierre-des-Corps(gare d'arrivée), la distance est bien égale à 2711.64
print("\n")
#Je fais un saut à la ligne pour que ce soit plus lisible et plus visuel 
print("Test 2 : distance entre toto et tata")
#Affiche test 2 qui émet la distance entre toto et tata
assert(distances("toto","tata"))==-1
#Je fais une vérification que la distance entre la gare toto (gare de départ), et la gare tata(gare d'arrivée), n'existe pas et donc renvoie -1 
print("\n")
#Je fais un saut à la ligne pour que ce soit plus lisible et plus visuel 
print("Test 3 : distance entre Blois - Chambord et Onzain - Chaumont-sur-Loire")
#Affiche test 3 qui émet la distance entre Blois-Chambord et Onzain-Chaumont-sur-Loire
assert(distances("Blois - Chambord","Onzain - Chaumont-sur-Loire"))==15066.716
#Je fais une vérification que la distance entre la gare Blois-Chambord (gare de départ), et la gare Onzain - Chaumont-sur-Loire(gare d'arrivée), la distance est bien égale à 15066.716