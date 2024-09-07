"""
Exemple :

Saisir:

Entrez le premier chiffre : 10

Entrez le deuxième chiffre : 5

Entrez l'opérateur (+, -, *, /) : *

Sortir:

Le résultat est: 50


Instructions

Ouvrez un nouveau fichier Python dans votre éditeur de code préféré.
Définissez une fonction appelée « calculatrice » qui prend deux arguments, « num1 » et « num2 ».
Dans la fonction, demandez à l'utilisateur de saisir un opérateur (+, -, *, /).
Utilisez des instructions conditionnelles pour déterminer l’opération à effectuer en fonction de la saisie de l’utilisateur.
Renvoie le résultat de l'opération.
Appelez la fonction calculatrice avec deux nombres et imprimez le résultat.
Gérer les cas où l'utilisateur saisit des opérateurs non valides ou tente de diviser par zéro.
Note:

Vous souhaiterez peut-être utiliser une boucle « while » pour permettre à l'utilisateur de lancer les dés plusieurs fois, ou pour ajouter des messages pour rendre le programme plus convivial.
"""
num1 = int(input("Saisir le nombre 1 :"))
num2 = int(input("Saisir le nombre 2 :"))


def play():
    jouer = int(input("Voulez vous continuer à calculer : \n Taper 1 pour Continuer \n Taper 0 pour Quitter :"))
    while jouer == 1:
        num1 = int(input("Saisir le nombre 1 :"))
        num2 = int(input("Saisir le nombre 2 :"))
        calculatrice(num1, num2)
        jouer = int(input("Voulez vous continuer à calculer : \n Taper 1 pour Continuer \n Taper 0 pour Quitter :"))

    print("Merci à la prochaine fois.")


def calculatrice(num1, num2):
    operateur = str(input("Entrez l'opérateur (+, -, *, /) : "))
    if operateur == "+":
        resultat = num1 + num2
        print("Vous avez choisi de faire une addition.")
        print()
        print("Le resultat de : ", num1, "+", num2, " = ", resultat)
    elif operateur == "-":
        resultat = num1 - num2
        print("Vous avez choisi de faire une soustraction.")
        print()
        print("Le resultat de : ", num1, "-", num2, " = ", resultat)
    elif operateur == "*":
        resultat = num1 * num2
        print("Vous avez choisi de faire une multiplication.")
        print()
        print("Le resultat de : ", num1, "*", num2, " = ", resultat)
    elif operateur == "/":
        if num2 == 0:
            print("Erreur, on peut pas divisé un nombre par 0")
        else:
            resultat = num1 / num2
            print("Vous avez choisi de faire une division.")
            print()
            print("Le resultat de : ", num1, "/", num2, " = ", resultat)
    else:
        print("Ce que vous venez de saisir n'est pas un opérateur de calcul. ")


calculatrice(num1, num2)
play()