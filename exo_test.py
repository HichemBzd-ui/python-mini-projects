chaine = input("Entrez une chaine: ")
charactere = input("Entrez une charactere: ")
if charactere in chaine:
    print(f'Oui {charactere} est presnet dans {chaine}')
else:
    print(f"Non le {charactere} n'est pas presnet dans {chaine} ")