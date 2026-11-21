from day4_ex import etudiants_listes
from day4_ex import etudiants_tuple
from day4_ex import etudiants_dict
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

data_type_validation(etudiants_listes);


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


print(competences)


def set_methods(competences):

    # 1. DATA OUTPUT
    print("\n--- DATA OUTPUT ---")
    print("Set :", competences)
    print("Type :", type(competences))
    print("Length :", len(competences))

    # 2. ADD()
    print("\n--- ADD ---")
    competences.add("Java")
    print(competences)

    # 3. UPDATE()
    print("\n--- UPDATE ---")
    competences.update(["HTML", "CSS", "JavaScript"])
    print(competences)

    # 4. REMOVE()
    print("\n--- REMOVE ---")
    competences.remove("Git")
    print(competences)

    # 5. DISCARD()
    print("\n--- DISCARD ---")
    competences.discard("PHP")
    print(competences)

    # 6. POP()
    print("\n--- POP ---")
    removed = competences.pop()
    print("Removed :", removed)

    # 7. COPY()
    print("\n--- COPY ---")
    competences_copy = competences.copy()
    print(competences_copy)

    # 8. UNION()
    print("\n--- UNION ---")
    autres = {"Java", "PHP", "SQL"}
    print(competences.union(autres))

    # 9. INTERSECTION()
    print("\n--- INTERSECTION ---")
    print(competences.intersection(autres))

    # 10. DIFFERENCE()
    print("\n--- DIFFERENCE ---")
    print(competences.difference(autres))

    # 11. SYMMETRIC DIFFERENCE()
    print("\n--- SYMMETRIC DIFFERENCE ---")
    print(competences.symmetric_difference(autres))

    # 12. ISSUBSET()
    print("\n--- ISSUBSET ---")
    print({"Python", "SQL"}.issubset(competences))

    # 13. ISSUPERSET()
    print("\n--- ISSUPERSET ---")
    print(competences.issuperset({"Python"}))

    # 14. ISDISJOINT()
    print("\n--- ISDISJOINT ---")
    print(competences.isdisjoint({"Ruby", "PHP"}))

    # 15. IN / NOT IN
    print("\n--- IN / NOT IN ---")
    print("Python" in competences)
    print("PHP" not in competences)

    # 16. LOOP / ENUMERATE
    print("\n--- LOOP ---")
    for index, competence in enumerate(competences, start=1):
        print(index, competence)

    # 17. FILTER()
    print("\n--- FILTER ---")
    python_competences = set(filter(
        lambda x: "P" in x,
        competences
    ))
    print(python_competences)

    # 18. CLEAR()
    print("\n--- CLEAR ---")
    temporary_set = competences.copy()
    temporary_set.clear()
    print(temporary_set)


set_methods(competences)



print(registre_etudiants)


def nested_dictionary_methods(registre_etudiants):

    # 1. DATA OUTPUT
    print("\n--- DATA OUTPUT ---")
    print(registre_etudiants)
    print("Type :", type(registre_etudiants))
    print("Length :", len(registre_etudiants))

    # 2. KEYS()
    print("\n--- KEYS ---")
    print(registre_etudiants.keys())

    # 3. VALUES()
    print("\n--- VALUES ---")
    print(registre_etudiants.values())

    # 4. ITEMS()
    print("\n--- ITEMS ---")
    for student_id, student_info in registre_etudiants.items():
        print(student_id, student_info)

    # 5. GET()
    print("\n--- GET ---")
    print(registre_etudiants.get("ETUD-001"))
    print(registre_etudiants.get("ETUD-999", "Not found"))

    # 6. ACCESS NESTED VALUE
    print("\n--- NESTED ACCESS ---")
    print(registre_etudiants["ETUD-001"].get("nom"))

    # 7. UPDATE()
    print("\n--- UPDATE ---")
    registre_etudiants["ETUD-001"].update({
        "classe": "B",
        "age": 20
    })
    print(registre_etudiants["ETUD-001"])

    # 8. SETDEFAULT()
    print("\n--- SETDEFAULT ---")
    registre_etudiants["ETUD-002"].setdefault("ville", "Rabat")
    print(registre_etudiants["ETUD-002"])

    # 9. POP()
    print("\n--- POP ---")
    temporary = registre_etudiants.copy()
    removed = temporary.pop("ETUD-003")
    print("Removed :", removed)

    # 10. COPY()
    print("\n--- COPY ---")
    registre_copy = registre_etudiants.copy()
    print(registre_copy)

    # 11. ENUMERATE()
    print("\n--- ENUMERATE ---")
    for index, (student_id, info) in enumerate(
        registre_etudiants.items(), start=1
    ):
        print(index, student_id, info["nom"])

    # 12. FILTER()
    print("\n--- FILTER ---")
    students_A = dict(filter(
        lambda item: item[1]["classe"] == "A",
        registre_etudiants.items()
    ))
    print(students_A)

    # 13. MAP()
    print("\n--- MAP ---")
    names = list(map(
        lambda item: item[1]["nom"],
        registre_etudiants.items()
    ))
    print(names)

    # 14. ANY() / ALL()
    print("\n--- ANY / ALL ---")
    print(any(
        info["classe"] == "A"
        for info in registre_etudiants.values()
    ))

    print(all(
        "nom" in info
        for info in registre_etudiants.values()
    ))

    # 15. IN / NOT IN
    print("\n--- IN / NOT IN ---")
    print("ETUD-001" in registre_etudiants)
    print("ETUD-999" not in registre_etudiants)

    # 16. CLEAR()
    print("\n--- CLEAR ---")
    temporary.clear()
    print(temporary)


nested_dictionary_methods(registre_etudiants)



print(Etudiant)

def namedtuple_methods(etudiants):

    # 1. DATA OUTPUT
    print("\n--- DATA OUTPUT ---")
    print(etudiants)
    print(type(etudiants[0]))

    # 2. ACCESS BY NAME
    print("\n--- ACCESS BY NAME ---")
    print(etudiants[0].nom)
    print(etudiants[0].moyenne)

    # 3. ACCESS BY INDEX
    print("\n--- ACCESS BY INDEX ---")
    print(etudiants[0][0])
    print(etudiants[0][1])

    # 4. _FIELDS
    print("\n--- _FIELDS ---")
    print(Etudiant._fields)

    # 5. _ASDICT()
    print("\n--- _ASDICT ---")
    print(etudiants[0]._asdict())

    # 6. _REPLACE()
    print("\n--- _REPLACE ---")
    updated = etudiants[0]._replace(moyenne=18)
    print(updated)

    # 7. _MAKE()
    print("\n--- _MAKE ---")
    new_student = Etudiant._make((5, "Mehdi", 14.5))
    print(new_student)

    # 8. COUNT()
    print("\n--- COUNT ---")
    print(etudiants[0].count("Amina"))

    # 9. INDEX()
    print("\n--- INDEX ---")
    print(etudiants[0].index("Amina"))

    # 10. ENUMERATE()
    print("\n--- ENUMERATE ---")
    for index, etudiant in enumerate(etudiants, start=1):
        print(index, etudiant.nom, etudiant.moyenne)

    # 11. MAP()
    print("\n--- MAP ---")
    names = list(map(lambda e: e.nom, etudiants))
    print(names)

    # 12. FILTER()
    print("\n--- FILTER ---")
    meilleurs = list(filter(
        lambda e: e.moyenne >= 15,
        etudiants
    ))
    print(meilleurs)

    # 13. MAX()
    print("\n--- MAX ---")
    best = max(etudiants, key=lambda e: e.moyenne)
    print(best)

    # 14. SORTED()
    print("\n--- SORTED ---")
    classement = sorted(
        etudiants,
        key=lambda e: e.moyenne,
        reverse=True
    )
    print(classement)

    # 15. ISINSTANCE()
    print("\n--- ISINSTANCE ---")
    print(isinstance(etudiants[0], Etudiant))
    print(isinstance(etudiants[0], tuple))

    # 16. ZIP()
    print("\n--- ZIP ---")
    ids = list(map(lambda e: e.id, etudiants))
    noms = list(map(lambda e: e.nom, etudiants))
    print(list(zip(ids, noms)))


namedtuple_methods(etudiants)