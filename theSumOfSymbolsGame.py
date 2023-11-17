# Auteurs: Mariam Elwa et Thanh Liem Huynh
# Date: 1 aout 2023

tabMystere= None

# La fonction element prend un parametre, id qui est une chaine de caracteres
# representant l'ID de l'element a recuperer. Elle recupere l'element du DOM
# qui a l'ID specifie. Le resultat est un objet DOM qui represente l'element
# trouve.

def element(id):
    return document.querySelector('#' + id) # retourner l'element DOM trouve


# La fonction case prend un parametre, index, qui est un entier representant
# l'index de la case de la grille a recuperer. Elle recupere l'element de la
# grille de jeu qui correspond a l'index specifie. Le resultat est un objet DOM
# qui represente l'element de la case de la grille.

def case(index):

    # retourner l'element DOM correspondant a l'id de la case specifie
    return element('case'+str(index))

#Étape 1 : Initialisation


# Les 5 images des symboles utilisées dans le jeu

symbole = ['symboles/circle.svg','symboles/cube.svg','symboles/penta.svg',
           'symboles/pyramide.svg','symboles/star.svg']


# La fonction sommeRangees prend trois paramètres, tab qui est une liste
# représentant la grille de jeu, nbRangees qui est un entier représentant le
# nombre de rangées dans la grille,et nbColonnes qui est un entier représentant
# le nombre de colonnes dans la grille. Elle retourne les sommes des nombres
# dans chaque rangée de la grille qui sont une liste d'entiers.

def sommeRangees(tab,nbRangees,nbColonnes):
    res = []         # liste vide pour stocker les sommes des rangees

    # Parcourir chaque rangee du tableau
    for i in range(nbRangees):
        somme = 0    # somme a 0 pour la rangee actuelle

        # Parcourir chaque colonne de la rangee actuelle
        for j in range(nbColonnes):
            somme += tab[i][j]  # ajouter la valeur de la case (i,j) a la somme

        # Ajouter la somme de la rangee actuelle a la liste des sommes
        res.append(somme)

    return res   # Retourner la liste des sommes des rangees


# La fonction sommeColonnes prend trois paramètres, tab qui est une liste
# représentant la grille de jeu, nbRangees qui est un entier représentant le
# nombre de rangées dans la grille,et nbColonnes qui est un entier représentant
# le nombre de colonnes dans la grille. Elle retourne les sommes des nombres
# dans chaque colonne de la grille qui sont une liste d'entiers.

def sommeColonnes(tab,nbRangees,nbColonnes):
    res = []          # liste vide pour stocker les sommes des colonnes

    # Parcourir chaque colonne du tableau
    for j in range(nbColonnes):
        somme = 0     # somme a 0 pour la colonne actuelle

        # Parcourir chaque rangee de la colonne actuelle
        for i in range(nbRangees):
            somme += tab[i][j]  # ajouter la valeur de la case (i,j) a la somme

        # Ajouter la somme de la colonne actuelle a la liste des sommes
        res.append(somme)

    return res   # Retourner la liste des sommes des colonnes


# La fonction tabIndexAlea  prend deux paramètres, nbRangees qui est un entier
# représentant le nombre de rangées dans la grille,et nbColonnes qui est un
# entier représentant le nombre de colonnes dans la grille. Elle génere une
# grille aléatoire d'index pour les symboles utilisés dans le jeu, le résultat
# est une liste.

def tabIndexAlea(nbRangees,nbColonnes):

    # Tableau 1D initialise avec des zeros de longueur nbRangees
    tab = [0]*nbRangees

    # Remplir chaque element du tableau 1D avec un nouveau tableau 1D
    # initialise avec des zeros de longueur nbColonnes
    for i in range(nbRangees):
        tab[i] = [0]*nbColonnes

    # Parcourir chaque element du tableau 2D (rangee et colonne) pour y placer
    # un nombre aleatoire entre 0 et 4 inclus (qui represente le type de
    # symbole a placer dans la case)
    for i in range(nbRangees):
        for j in range(nbColonnes):
            tab[i][j] = math.floor(5*random())

    # Retourner tableau 2D contenant les types de symboles aleatoires
    return tab


#Générer cinq nombre entiers positifs de 1 à 20 et les associer à
#chacun des 5 symboles


# La fonction nbMystere prend un paramètre, tabIndex qui est une liste
# représentant la grille d'index pour les symboles. Elle génère la grille
# mystère en associant les nombres aux symboles, le résultat est une liste.

def nbMystere(tabIndex):
    # Determiner le nombre de rangees du tableau 2D 'tabIndex'
    nbRangees = len(tabIndex)

    # Determiner le nombre de colonnes du tableau 2D'tabIndex'
    nbColonnes = len(tabIndex[0])

    tab = [0]*nbRangees   # Nouveau tableau 2D
    for i in range(nbRangees):
        tab[i] = [0]*nbColonnes

    # Tableau contenant 5 elements initialises a 0
    cinqNombres = [0]*5

    # Generer 5 nombres aleatoires entre 1 et 20 inclus et les stocker dans le
    # tableau 'cinqNombres'
    for i in range(5):
        cinqNombres[i] = math.floor(20*random()+1)

    # Parcourir chaque rangee du tableau 2D 'tabIndex'
    for i in range(nbRangees):

        # Parcourir chaque colonne du tableau 2D 'tabIndex'
        for j in range(nbColonnes):

            # Recuperer la valeur 'index' de la case (i,j) de 'tabIndex'
            index = tabIndex[i][j]

            # En fonction de la valeur 'index', attribuer a la case
            # correspondante de 'tab' un nombre associe depuis le tableau
            # 'cinqNombres'
            if index == 0:
                tab[i][j] = cinqNombres[0]
            elif index == 1:
                tab[i][j] = cinqNombres[1]
            elif index == 2:
                tab[i][j] = cinqNombres[2]
            elif index == 3:
                tab[i][j] = cinqNombres[3]
            else:
                tab[i][j] = cinqNombres[4]

    #Retourner tableau 2D 'tab' qui contient les nombres associes a chaque case
    return tab



# La fonction clic prend un paramètre, index  qui est un entier
# représentant l'index de la case cliquee. Elle permet de demander a
# l'utilisateur de saisir un nombre de 1 a 20. Elle retourne un entier, qui est
# le nombre saisi par l'utilisateur.

def clic(index):

    global tabMystere

    # Demander a l'utilisateur de saisir un nombre
    nbr = int(prompt("Veuillez saisir un nombre de 1 a 20."))

    # si la valeur de nbr est entre 1 et 20(inclus)
    if 1<= nbr <=20:

        #obtenir les coordonnees de la case
        i= index // 6 # determiner l'indice de la rangee i
        j= index % 6  # determiner l'indice de la colonne j

        #mettre a jour tabMystere avec le nombre saisie a la position (i,j)
        tabMystere[i][j]=nbr

        # mettre a jour les sommes des rangées de la grille mystère
        tabSommeRangee = sommeRangees(tabMystere,5,5)

        # mettre a jour les sommes des colonnes de la grille mystère
        tabSommeColonne = sommeColonnes(tabMystere,5,5)

        # Mettre a jour la liste des index des cases correspondants aux sommes des rangees
        indexR = [5,11,17,23,29]

        # Mettre a jour la liste des index des cases correspondants aux sommes des colonnes
        indexC = [30,31,32,33,34]

        # Mettre a jour les valeurs des sommes des rangees dans les cases
        for i in range(5):
            # definir contenu HTML de la case avec la somme de la rangee
            case(indexR[i]).innerHTML = str(tabSommeRangee[i])
            # Mettre a jour les valeurs des sommes des colonnes dans les cases
            for j in range(5):
                # definir contenu HTML de la case avec la somme de la colonne
                case(indexC[j]).innerHTML = str(tabSommeColonne[j])

            # verifier si le joueur a gagne
            victoire(tabMystere,tabSommeRangee,tabSommeColonne)

   # sinon afficher ce message d'erreur
    else:
        alert("Erreur! Veuillez saisir un nombre de 1 a 20 SVP")


#La procedure victoire prend trois parametres,tabMystere qui est une liste
#representant le jeu,tabSommeRangee qui est une liste representant les sommes
#des rangees attendues, et tabSommeColonne qui est une liste representant les
#sommes des colonnes attendues. Elle verifie si les sommes des rangees et des
#colonnes de tabMystere correspondent aux valeurs dans tabSommeRangee et
#tabSommeColonne, pour savoir s'il y a une victoire.

def victoire(tabMystere,tabSommeRangee,tabSommeColonne):

    #sommes pour chaque rangee
    for i in range(5):
        sommeRangee=0

        #calculer la somme des elements de la rangee actuelle
        for j in range (5):
            sommeRangee+=tabMystere[i][j]

            #si la somme de la rangee actuelle n'est pas egal a la valeur
            #attendue dans tabSommeRangee
            if sommeRangee!= tabSommeRangee[i]:
                return defaite() # retourner que le joueur a perdu

    #sommes pour chaque colonne
    for j in range(5):
        sommeColonne=0

        #calculer la somme des elements de la colonne actuelle
        for i in range (5):
            sommeColonne+=tabMystere[i][j]

            #si la somme de la colonne actuelle n'est pas egal a la valeur
            #attendue dans tabSommeColonne
            if sommeColonne!= tabSommeColonne[j]:
                return defaite() # retourner que le joueur a perdu

    # Si toutes les sommes sont egales aux valeurs attendues, imprimer que le
    # joueur a gagne
    print("Vous avez gagne!")


# La procedure defaite ne prend aucun parametre. Elle affiche un message pour
# indiquer que le joueur a perdu le jeu.

def defaite():
    print("Vous avez perdu!")


#La procédure init ne prend aucun paramètre. Elle initialise le jeu.
def init():

    global tabMystere

    # générer une grille aléatoire d'index pour les symboles
    tabIndex = tabIndexAlea(5,5)

    # générer la grille mystère en associant les nombres aux symboles
    tabMystere = nbMystere(tabIndex)

    # Calculer les sommes des rangées de la grille mystère
    tabSommeRangee = sommeRangees(tabMystere,5,5)

    # Calculer les sommes des colonnes de la grille mystère
    tabSommeColonne = sommeColonnes(tabMystere,5,5)


    # Interface graphique du jeu
    main = document.querySelector("#main")
    main.innerHTML = """
      <style>
        #jeu table { float: none; }
        #jeu table td {
            border: 1px solid black;
            padding: 1px 2px;
            width: 80px;
            height: 80px;
            font-family: Helvetica;
            font-size: 20px;
            text-align: center;
        }
        #jeu table td img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            object-fit: contain;
            width: 80%;
            height: 80%;
        }
      </style>
      <div id="jeu">

        <button onclick="init()">Nouvelle partie</button><br>

        <h1 style="color: red">Jouer!</h1>

        <table>
          <tr>
            <td id="case0" onclick="clic(0)"><img src=' """ + \
    symbole[tabIndex[0][0]]+ """ '></td>
            <td id="case1" onclick="clic(1)"><img src=' """ + \
    symbole[tabIndex[0][1]]+ """ '></td>
            <td id="case2" onclick="clic(2)"><img src=' """ + \
    symbole[tabIndex[0][2]]+ """ '></td>
            <td id="case3" onclick="clic(3)"><img src=' """ + \
    symbole[tabIndex[0][3]]+ """ '></td>
            <td id="case4" onclick="clic(4)"><img src=' """ + \
    symbole[tabIndex[0][4]]+ """ '></td>
            <td id="case5"></td>
          </tr>
          <tr>
            <td id="case6" onclick="clic(6)"><img src=' """ + \
    symbole[tabIndex[1][0]]+ """ '></td>
            <td id="case7" onclick="clic(7)"><img src=' """ + \
    symbole[tabIndex[1][1]]+ """ '></td>
            <td id="case8" onclick="clic(8)"><img src=' """ + \
    symbole[tabIndex[1][2]]+ """ '></td>
            <td id="case9" onclick="clic(9)"><img src=' """ + \
    symbole[tabIndex[1][3]]+ """ '></td>
            <td id="case10" onclick="clic(10)"><img src=' """ + \
    symbole[tabIndex[1][4]]+ """ '></td>
            <td id="case11"></td>
          </tr>
          <tr>
            <td id="case12" onclick="clic(12)"><img src=' """ + \
    symbole[tabIndex[2][0]]+ """ '></td>
            <td id="case13" onclick="clic(13)"><img src=' """ + \
    symbole[tabIndex[2][1]]+ """ '></td>
            <td id="case14" onclick="clic(14)"><img src=' """ + \
    symbole[tabIndex[2][2]]+ """ '></td>
            <td id="case15" onclick="clic(15)"><img src=' """ + \
    symbole[tabIndex[2][3]]+ """ '></td>
            <td id="case16" onclick="clic(16)"><img src=' """ + \
    symbole[tabIndex[2][4]]+ """ '></td>
            <td id="case17"></td>
          </tr>
          <tr>
            <td id="case18" onclick="clic(18)"><img src=' """ + \
    symbole[tabIndex[3][0]]+ """ '></td>
            <td id="case19" onclick="clic(19)"><img src=' """ + \
    symbole[tabIndex[3][1]]+ """ '></td>
            <td id="case20" onclick="clic(20)"><img src=' """ + \
    symbole[tabIndex[3][2]]+ """ '></td>
            <td id="case21" onclick="clic(21)"><img src=' """ + \
    symbole[tabIndex[3][3]]+ """ '></td>
            <td id="case22" onclick="clic(22)"><img src=' """ + \
    symbole[tabIndex[3][4]]+ """ '></td>
            <td id="case23"></td>
          </tr>
          <tr>
            <td id="case24" onclick="clic(24)"><img src=' """ + \
    symbole[tabIndex[4][0]]+ """ '></td>
            <td id="case25" onclick="clic(25)"><img src=' """ + \
    symbole[tabIndex[4][1]]+ """ '></td>
            <td id="case26" onclick="clic(26)"><img src=' """ + \
    symbole[tabIndex[4][2]]+ """ '></td>
            <td id="case27" onclick="clic(27)"><img src=' """ + \
    symbole[tabIndex[4][3]]+ """ '></td>
            <td id="case28" onclick="clic(28)"><img src=' """ + \
    symbole[tabIndex[4][4]]+ """ '></td>
            <td id="case29"></td>
          </tr>
          <tr>
            <td id="case30"></td>
            <td id="case31"></td>
            <td id="case32"></td>
            <td id="case33"></td>
            <td id="case34"></td>
            <td id="case35"></td>
          </tr>
        </table>
      </div>"""


    # Liste des index des cases correspondants aux sommes des rangees
    indexR = [5,11,17,23,29]

    # Liste des index des cases correspondants aux sommes des colonnes
    indexC = [30,31,32,33,34]

    # Mettre a jour les valeurs des sommes des rangees dans les cases
    for i in range(5):
        # definir contenu HTML de la case avec la somme de la rangee
        case(indexR[i]).innerHTML = str(tabSommeRangee[i])

    # Mettre a jour les valeurs des sommes des colonnes dans les cases
    for j in range(5):
        # definir contenu HTML de la case avec la somme de la colonne
        case(indexC[j]).innerHTML = str(tabSommeColonne[j])