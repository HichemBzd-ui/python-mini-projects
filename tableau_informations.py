tableau_haut = "[Nom]\t│[Prenom]\t│[Age]"
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))

print(tableau_haut)
print(f"{nom}\t│{prenom}\t│{age}")