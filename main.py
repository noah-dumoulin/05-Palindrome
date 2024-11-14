#### Fonction secondaire
'''permet de renvoyer si une chaine de caractères est un palindrome ou non'''
def nettoyer(p):
    '''nettoie la chaine de caractères passées en paramètres 
    (retire les espaces accents et majuscules)'''
    p=p.lower()
    p=p.translate(str.maketrans('éèêëçàâäîïùöô','eeeecaaaiiuoo'))
    p = p.translate({ord(i): None for i in ' ,-?;.:!\''})
    return p
def ispalindrome(p):
    '''verifie si la string passée en paramètres est un palindrome'''
    # votre code ici
    p=nettoyer(p)
    return p==p[::-1]
#### Fonction principale


def main():
    '''appel de la fonction secondaire et affichage du résultat'''
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
