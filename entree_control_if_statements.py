# if : teste une première condition
# elif : teste une autre condition si les précédentes sont fausses
# else : exécute ce bloc si toutes les conditions précédentes sont fausses

age = int(input("What is your age?"))
with_adult = input("Are you with an adult ?")
if age >= 18:
    print("You can enter to the stadium")
elif age < 18 and with_adult=="yes" and "Yes": # == pour comparer
    print("You are with an adult so you can enter to the stadium")
else:
    print("You can't enter to the stadium because your age is less than 18 and you are not with an adult")
D