# 1. Initializing collections (simulating array/list/tuple concepts)
number_tuple = [1, 2, 4]  # Ruby arrays handle all sequence operations
list_number = [1, 2, 4]

# 2. User Input
print "entrer un nombre = "
input_number = gets.to_i   # Reads input and converts directly to integer

# 3. Type conversions
float_input = input_number.to_f
string_number = input_number.to_s

# 4. Square root calculation (input_number ** 0.5)
square_input_number = Math.sqrt(input_number)

# 5. Look up element in the sequence
exists = list_number.include?(input_number)

if exists
  # Find the array index
  index = list_number.index(input_number)
  puts "nombre existant #{input_number}, indice #{index}"

  # 6. Verification of data types using .class
  puts " du tuple, #{number_tuple.class}"
  puts " du list, #{list_number.class}"
  puts " input_number, #{input_number.class}"
  puts " float input, #{float_input.class}"
  puts " string_number, #{string_number.class}"
  puts " square_input_number, #{square_input_number.class}"

  # 7. Mathematical operations using the index
  puts "somme = #{input_number + index}"
  puts "substraction = #{input_number - index}"
  puts "multiplication = #{input_number * index}"

  # Arithmetic protections against dividing by zero index
  if index != 0
    puts "division classic = #{input_number.to_f / index}"
    puts "division entiere = #{input_number / index}"
    puts "division (modulo-reste) = #{input_number % index}"
    
    # Custom array display simulating Python's divmod()
    divmod_result = input_number.divmod(index)
    puts "division = (#{divmod_result[0]}, #{divmod_result[1]})"
  else
    puts "Cannot divide by an index of 0!"
  end

else
  puts "nombre non existant essayer d'entrer un nombre dans la liste"
end
