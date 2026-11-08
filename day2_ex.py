
startup_numbers = 1, 2, 3

input_number = int(input('entrer un nombre valide = '));


list_number = list(startup_numbers);
float_input = float(input_number);
string_number = str(input_number);
square_input_number = input_number**0.5;

# verification d'existence dans la liste startup

def existence_verification(input_number):
    if input_number in startup_numbers:
        
        print(f'"nombre existant {input_number}, indice {startup_numbers.index(input_number)}')

    else:
        print(f"nombre introuvale entrer un nombre dans l'ensemble, {list(number)}")



# verification du type

def interlopation_type():
    print("\n--- Interlopation DES TYPES ---")

    print(f"Type du tuple : {type(startup_numbers)}")
    print(f"Type de la liste : {type(list_number)}")
    print(f"Type input_number : {type(input_number)}")
    print(f"Type float_input : {type(float_input)}")
    print(f"Type string_number : {type(string_number)}")
    print(f"Type square_input_number : {type(square_input_number)}")

# creation automatique du liste et ajoute de chaque nombre

input_array_size = int(input('entrer la taille du liste = '));

input_numbers = []

def array_list_handle():
    for i in range(1, input_array_size + 1):
        i = int(input(f"entrer le nombre {i} de la liste = "))
        input_numbers.append(i)
        print(f"list : {input_numbers}")
        print(f"number {i} indice : {input_numbers.index(i)}")


        

#  Operations mathematiques
def calculate(a, b):
    print("\n--- OPERATIONS MATHEMATIQUES ---")

    print(f"Somme = {a + b}")
    print(f"Soustraction = {a - b}")
    print(f"Multiplication = {a * b}")

    if b != 0:
        print(f"Division classique = {a / b}")
        print(f"Division entiere = {a // b}")
        print(f"Modulo = {a % b}")
        print(f"Divmod = {divmod(a, b)}")
    else:
        print("Division impossible : division par zero.")


# appel des fonctions

existence_verification(input_number);

verification_type();

array_list_handle();

calculate(input_number, startup_numbers.index(input_number));