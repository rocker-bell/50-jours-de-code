
require 'set'
require 'date'

# 1. Array of hashes (equivalent to Python dictionaries)
etudiants_dict = [
  { id: 1, nom: "Amina", age: 20, moyenne_generale: 15.5 },
  { id: 2, nom: "Youssef", age: 22, moyenne_generale: 13.8 },
  { id: 3, nom: "Sofia", age: 21, moyenne_generale: 16.2 },
  { id: 4, nom: "Amine", age: 23, moyenne_generale: 11.4 }
]

# Loop through students
def etudiants_dict_loop(etudiants_dict)
  etudiants_dict.each_with_index do |etudiant, index|

    if etudiant[:id] == 1
      puts "Dictionnaire : #{etudiant}"
    end

    etudiant.each do |key, value|
      puts "key : #{key} and value : #{value}"
    end

    puts "dict : #{etudiant}, index : #{index}"
  end
end

etudiants_dict_loop(etudiants_dict)

# 2. List of lists (Array of Arrays)
etudiants_listes = [
  [1, "Amina", 20, 15.5],
  [2, "Youssef", 22, 13.8],
  [3, "Sofia", 21, 16.2],
  [4, "Amine", 23, 11.4]
]

# 3. Tuple equivalent: frozen Array
etudiants_tuple = [
  [1, "Amina", 20, 15.5],
  [2, "Youssef", 22, 13.8],
  [3, "Sofia", 21, 16.2],
  [4, "Amine", 23, 11.4]
].map(&:freeze).freeze

# 4. Set: automatically removes duplicates
competences = Set.new(["Python", "SQL", "Git", "Python", "Excel"])

puts competences.inspect

# 5. Nested Hash
registre_etudiants = {
  "ETUD-001" => { nom: "Amina", classe: "A" },
  "ETUD-002" => { nom: "Youssef", classe: "B" },
  "ETUD-003" => { nom: "Sofia", classe: "A" }
}

puts registre_etudiants["ETUD-003"][:nom]

# 6. Date
date_inscription = Date.new(2026, 9, 1)

puts "Inscrit le : #{date_inscription.strftime('%d/%m/%Y')}"

# 7. Namedtuple equivalent: Struct
Etudiant = Struct.new(:id, :nom, :moyenne)

etudiant_1 = Etudiant.new(10, "Amine", 14.5)

puts etudiant_1.nom
puts etudiant_1.moyenne
