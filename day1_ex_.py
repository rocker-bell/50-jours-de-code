# cette exercice envisione plusieurs utilsation des  type du donnes basic est l'interlopation entre eux

#tuple
number = 1, 2, 4

#liste
list_number = list(number)

#input du nombe
input_number = int(input("entrer un nombre =  "));

#conversion du type

float_input = float(input_number);
string_number = str(input_number);
square_input_number = input_number**0,5

#utilisation conditionnelle
if input_number in number:
    print(f"nombre existant {input_number}, indice {number.index(input_number)}")
else:
    print(f"nombre introuvale entrer un nombre dans l'ensemble, {list(number)}")

# verification du type
print(f'type du tuple, {type(number)}')
print(f'type du list, {type(list_number)}')
print(f'type input_number, {type(input_number)}')
print(f'type float input, {type(float_input)}')
print(f'type string_number, {type(string_number)}')
print(f'type square_input_number, {type(square_input_number)}')

# operation mathematics

#somme (nombre est indice)

print(f'somme = {input_number + number.index(input_number)}')

# substraction

print(f'substraction = {input_number - number.index(input_number)}')

#multiplication

print(f'multiplication = {input_number * number.index(input_number)}')

# division classic
print(f'division classic = {input_number / number.index(input_number)}')
#division entiere
print(f'division entiere = {input_number // number.index(input_number)}')
#modulo reste
print(f'division (modulo-reste) = {input_number % number.index(input_number)}')
#divmod
print(f'division = {divmod(input_number, number.index(input_number))}')

#NB : nombre doit etre present dans le tuple