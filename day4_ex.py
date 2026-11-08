# Pratique des différentes méthodes Python sur les listes, les dictionnaires et les tuples


fruits_array = ['Pomme', 'Banane', 'Kiwi', 'Orange', 'Myrtille', 'Mûre'];
colors_array = ['Rouge', 'Jaune', 'Vert', 'Orange', 'Bleu', 'Noir'];

print(fruits_array);

print(type(fruits_array));

fruits_array.append('citron');

print(fruits_array);


fruits_array.remove('citron');

print(fruits_array);


fruits_array.pop(fruits_array.index('Orange'));

print(fruits_array);



def filter_leslistes(x):
    for array in [fruits_array, colors_array]:
        if x in array:
            print(f"x : {x} se trouve dans la position : {array.index(x)}")
            return True

    return False


liste_filter = list(filter(filter_leslistes, ['Kiwi', 'Orange', 'Vert', 'Bleu', 'Blanche']))

print(liste_filter)


# Une liste contenant des dictionnaires d'étudiants
etudiants_dict = [
    {"id": 1, "nom": "Amina", "age": 20, "moyenne_generale": 15.5},
    {"id": 2, "nom": "Youssef", "age": 22, "moyenne_generale": 13.8},
    {"id": 3, "nom": "Sofia", "age": 21, "moyenne_generale": 16.2},
    {"id": 4, "nom": "Amine", "age": 23, "moyenne_generale": 11.4}
]

def etudiants_dict_loop(etudiants_dict):
    for dict in etudiants_dict:
        for key, value in dict.items():
            if key == "id" and value == 1:
                print (f"dictionaire : {dict}")
            else:
                print(f"key : {key} and value : {value} doesnt exist ")
        print(f"dict {dict}, index : {etudiants_dict.index(dict)}")

etudiants_dict_loop(etudiants_dict);



# Liste de listes
etudiants_listes = [
    [1, "Amina", 20, 15.5],
    [2, "Youssef", 22, 13.8],
    [3, "Sofia", 21, 16.2],
    [4, "Amine", 23, 11.4]
]


# Un tuple global contenant des sous-tuples d'étudiants
etudiants_tuple = (
    (1, "Amina", 20, 15.5),
    (2, "Youssef", 22, 13.8),
    (3, "Sofia", 21, 16.2),
    (4, "Amine", 23, 11.4)
)

# Un ensemble de badges ou de compétences d'étudiants (les doublons sont automatiquement supprimés)
competences = {"Python", "SQL", "Git", "Python", "Excel"}


# Dictionnaire de dictionnaires
registre_etudiants = {
    "ETUD-001": {"nom": "Amina", "classe": "A"},
    "ETUD-002": {"nom": "Youssef", "classe": "B"},
    "ETUD-003": {"nom": "Sofia", "classe": "A"}
}

# Accès direct ultra-rapide grâce à la clé
print(registre_etudiants["ETUD-003"]["nom"])  # Sortie : Sofia


# objet de temps

from datetime import datetime, date

# Stockage d'une date précise (Année, Mois, Jour)
date_inscription = date(2026, 9, 1)
print(f"Inscrit le : {date_inscription.strftime('%d/%m/%Y')}") 
# Sortie : Inscrit le : 01/09/2026

# namedtuple

from collections import namedtuple

# On définit le modèle structurel
Etudiant = namedtuple('Etudiant', ['id', 'nom', 'moyenne'])

# On crée une instance
etudiant_1 = Etudiant(id=10, nom="Amine", moyenne=14.5)

# Accès très propre aux données
print(etudiant_1.nom)      # Sortie : Amine
print(etudiant_1.moyenne)  # Sortie : 14.5
