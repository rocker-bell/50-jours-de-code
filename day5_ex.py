import csv, json

from day4_ex import etudiants_dict

from day4_ex import etudiants_listes

from day4_ex import etudiants_tuple

from day4_ex import competences

from day4_ex import registre_etudiants

from day4_ex import Etudiant


# pratique list
print(etudiants_listes)

def data_type_validation(etudiants_listes):

    # 1. Data output
    print("Liste :", etudiants_listes)
    print("Longueur :", len(etudiants_listes))
    print("Type :", type(etudiants_listes))

    print("Min :", min(etudiants_listes))
    print("Max :", max(etudiants_listes))

    print("Liste inversée :", list(reversed(etudiants_listes)))
    print("Liste triée :", sorted(etudiants_listes))

    # 2. Loop
    for index, student in enumerate(etudiants_listes):
        print(f"Student : {student}, Index : {index}")

    # 3. Array manipulation
    etudiants_listes.append([5, "mehdi", 23, 15])

    etudiants_listes.pop(0)

    # 4. Input
    etudiants_name = input("Entrer un nom d'étudiant : ")
    etudiants_name = etudiants_name.strip().capitalize()

    # 5. Search and remove
    if etudiants_name in etudiants_listes:
        etudiants_listes.remove(etudiants_name)
        print(f"{etudiants_name} supprimé.")
    else:
        print(f"{etudiants_name} introuvable dans la liste.")

    # 6. Sorting
    etudiants_listes.sort(
        key=str,
        reverse=True
    )

    print("Liste finale :", etudiants_listes)


data_type_validation(etudiants_listes)

print(etudiants_tuple)


print(etudiants_dict)


print(competences)


print(registre_etudiants)

print(Etudiant)