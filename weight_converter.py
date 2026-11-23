# python weight converter

# Kg to G => 1Kg = 1000g

poids = float(input("Entrez la valeur du poids: "))
unite = input("Kilogramme ou gramme? (kg / g) ")

if unite == "Kilogramme" or unite == "kg":
 poids = poids * 1000
 print(f"votre poids en gramme est de {round(poids)}g")
elif unite == "gramme" or unite == "g":
 poids = poids / 1000
 print(f"votre poids en kilogramme est de {round(poids)}Kg")
else:
 print("l'unité n'est pas valide")