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
    found = False

    for etudiants in etudiants_listes:
        for name in etudiants:

            if name == etudiants_name:
                etudiants_listes.remove(etudiants)
                print(f"{etudiants} supprimé.")
                found = True
                break

        if found:
            break

    if not found:
        print(f"{etudiants_name} introuvable dans la liste.")

    # 6. Sorting
    etudiants_listes.sort(
        key=str,
        reverse=True
    )

    print("Liste finale :", etudiants_listes)


data_type_validation(etudiants_listes)

print(etudiants_tuple)

def tuple_methods(etudiants_tuple):

    # 1. DATA OUTPUT
    print("\n--- DATA OUTPUT ---")
    print("Tuple :", etudiants_tuple)
    print("Length :", len(etudiants_tuple))
    print("Type :", type(etudiants_tuple))
    print("Min :", min(etudiants_tuple))
    print("Max :", max(etudiants_tuple))

    # 2. COUNT()
    print("\n--- COUNT ---")
    print("Occurrences of Amina :",
          etudiants_tuple.count((1, "Amina", 20, 15.5)))

    # 3. INDEX()
    print("\n--- INDEX ---")
    print("Index of Sofia :",
          etudiants_tuple.index((3, "Sofia", 21, 16.2)))

    # 4. LOOP
    print("\n--- LOOP ---")
    for etudiant in etudiants_tuple:
        print(etudiant)

    # 5. ENUMERATE()
    print("\n--- ENUMERATE ---")
    for index, etudiant in enumerate(etudiants_tuple, start=1):
        print(f"Index : {index}, Student : {etudiant}")

    # 6. SLICING
    print("\n--- SLICING ---")
    print("First student :", etudiants_tuple[0])
    print("Last student :", etudiants_tuple[-1])
    print("First two :", etudiants_tuple[:2])
    print("Reverse :", etudiants_tuple[::-1])

    # 7. IN / NOT IN
    print("\n--- IN / NOT IN ---")
    print("Amina exists :",
          any("Amina" in e for e in etudiants_tuple))

    print("Mehdi absent :",
          not any("Mehdi" in e for e in etudiants_tuple))

    # 8. MAP()
    print("\n--- MAP ---")
    noms = tuple(map(lambda e: e[1], etudiants_tuple))
    print("Students names :", noms)

    # 9. FILTER()
    print("\n--- FILTER ---")
    meilleurs = tuple(filter(
        lambda e: e[3] >= 15,
        etudiants_tuple
    ))
    print("Students with average >= 15 :", meilleurs)

    # 10. ZIP()
    print("\n--- ZIP ---")
    ids = (1, 2, 3, 4)
    noms = ("Amina", "Youssef", "Sofia", "Amine")

    print(tuple(zip(ids, noms)))

    # 11. ANY() / ALL()
    print("\n--- ANY / ALL ---")
    print("Any average >= 16 :",
          any(e[3] >= 16 for e in etudiants_tuple))

    print("All students >= 10 :",
          all(e[3] >= 10 for e in etudiants_tuple))

    # 12. SORTED()
    print("\n--- SORTED ---")
    print("Sorted by average :",
          sorted(etudiants_tuple, key=lambda e: e[3]))

    print("Sorted descending :",
          sorted(etudiants_tuple,
                 key=lambda e: e[3],
                 reverse=True))

    # 13. TYPE VALIDATION
    print("\n--- ISINSTANCE ---")
    print(isinstance(etudiants_tuple, tuple))

    # 14. CONCATENATION
    print("\n--- CONCATENATION ---")
    new_student = (5, "Mehdi", 23, 14.5)
    new_tuple = etudiants_tuple + (new_student,)
    print(new_tuple)

    # 15. REPETITION
    print("\n--- REPETITION ---")
    print((1, 2) * 3)

    # 16. CONVERSION
    print("\n--- CONVERSION ---")
    print("Tuple to list :", list(etudiants_tuple))
    print("List to tuple :", tuple([1, 2, 3]))

    # 17. NESTED LOOP
    print("\n--- NESTED LOOP ---")
    for etudiant in etudiants_tuple:
        for element in etudiant:
            print(element, end=" | ")
        print()

tuple_methods(etudiants_tuple)

print(etudiants_dict)

def dictionary_methods(etudiants_dict):

    # 1. KEYS()
    print("\n--- KEYS ---")
    for etudiant in etudiants_dict:
        print(etudiant.keys())

    # 2. VALUES()
    print("\n--- VALUES ---")
    for etudiant in etudiants_dict:
        print(etudiant.values())

    # 3. ITEMS()
    print("\n--- ITEMS ---")
    for etudiant in etudiants_dict:
        for key, value in etudiant.items():
            print(f"{key} : {value}")

    # 4. GET()
    print("\n--- GET ---")
    for etudiant in etudiants_dict:
        print(etudiant.get("nom"))
        print(etudiant.get("ville", "Inconnue"))

    # 5. UPDATE()
    print("\n--- UPDATE ---")
    etudiants_dict[0].update({
        "age": 21,
        "ville": "Rabat"
    })
    print(etudiants_dict[0])

    # 6. POP()
    print("\n--- POP ---")
    removed_value = etudiants_dict[1].pop("age")
    print("Valeur supprimée :", removed_value)
    print(etudiants_dict[1])

    # 7. CLEAR()
    print("\n--- CLEAR ---")
    temporary_dict = etudiants_dict[0].copy()
    temporary_dict.clear()
    print("Dictionnaire vidé :", temporary_dict)

    # 8. COPY()
    print("\n--- COPY ---")
    etudiant_copy = etudiants_dict[2].copy()
    print("Original :", etudiants_dict[2])
    print("Copie :", etudiant_copy)

    # 9. SETDEFAULT()
    print("\n--- SETDEFAULT ---")
    etudiants_dict[3].setdefault("ville", "Casablanca")
    print(etudiants_dict[3])

    # Final output
    print("\n--- FINAL LIST ---")
    for etudiant in etudiants_dict:
        print(etudiant)


# Function execution
dictionary_methods(etudiants_dict)


print(competences)


print(registre_etudiants)

print(Etudiant)