
# Ensemble initial
startup_numbers = [1, 2, 3]

list_number = startup_numbers.dup

input_numbers = []

# Saisie du nombre
print "Entrer un nombre valide = "
input_number = gets.to_i

float_input = input_number.to_f
string_number = input_number.to_s
square_input_number = Math.sqrt(input_number)

# Verification d'existence
def existence_verification(input_number, startup_numbers)

    if startup_numbers.include?(input_number)

        index = startup_numbers.index(input_number)

        puts "Nombre existant #{input_number}, indice #{index}"

        return index

    else

        puts "Nombre introuvable. Entrez un nombre dans l'ensemble : #{startup_numbers}"

        return -1
    end
end

# Verification des types
def verification_type(
    startup_numbers,
    list_number,
    input_number,
    float_input,
    string_number,
    square_input_number
)

    puts "\n--- VERIFICATION DES TYPES ---"

    puts "Type du tableau : #{startup_numbers.class}"

    puts "Type de la liste : #{list_number.class}"

    puts "Type input_number : #{input_number.class}"

    puts "Type float_input : #{float_input.class}"

    puts "Type string_number : #{string_number.class}"

    puts "Type square_input_number : #{square_input_number.class}"

end

# Creation automatique de la liste
def array_list_handle(input_array_size, input_numbers)

    for i in 1..input_array_size

        print "Entrer le nombre #{i} de la liste = "

        number = gets.to_i

        input_numbers << number

        puts "List : #{input_numbers}"

        puts "Number #{number} indice : #{input_numbers.index(number)}"

    end

end

# Operations mathematiques
def calculate(a, b)

    puts "\n--- OPERATIONS MATHEMATIQUES ---"

    puts "Somme = #{a + b}"

    puts "Soustraction = #{a - b}"

    puts "Multiplication = #{a * b}"

    if b != 0

        puts "Division classique = #{a.to_f / b}"

        puts "Division entiere = #{a / b}"

        puts "Modulo = #{a % b}"

        puts "Divmod = #{a.divmod(b)}"

    else

        puts "Division impossible : division par zero."

    end

end

# Appel des fonctions
index = existence_verification(input_number, startup_numbers)

verification_type(
    startup_numbers,
    list_number,
    input_number,
    float_input,
    string_number,
    square_input_number
)

print "\nEntrer la taille de la liste = "

input_array_size = gets.to_i

array_list_handle(input_array_size, input_numbers)

if index != -1
    calculate(input_number, index)
end
