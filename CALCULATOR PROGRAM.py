operateurs = input("Veillez entrer l'opérateur (+,-,*,/) ")

num1 = float(input("Veillez entrer le premier numéro "))
num2 = float(input("Veillez entrer le second numéro "))

if operateurs == "+":
    result = num1 + num2
    print(round(result, 3))
elif operateurs == "-":
    result = num1 - num2
    print(round(result, 3))
elif operateurs == "*":
    result = num1 * num2
    print(round(result, 3))
elif operateurs == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operateurs} is not valid ")
