import json
import csv
import os

from day4_ex import (
    etudiants_listes,
    etudiants_tuple,
    etudiants_dict,
    competences,
    registre_etudiants,
    Etudiant,
    etudiants
)


# ==================================================
# CREATION DES DOSSIERS
# ==================================================

os.makedirs("sauvegarde/csv", exist_ok=True)
os.makedirs("sauvegarde/json", exist_ok=True)


# ==================================================
# 1. LIST OF LISTS - CSV
# ==================================================

def list_csv(data):

    print("\n--- LIST CSV ---")

    with open("sauvegarde/csv/etudiants_listes.csv",
              "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["id", "nom", "age", "moyenne"])
        writer.writerows(data)

    with open("sauvegarde/csv/etudiants_listes.csv",
              "r", encoding="utf-8") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)


# ==================================================
# 2. LIST OF LISTS - JSON
# ==================================================

def list_json(data):

    print("\n--- LIST JSON ---")

    with open("sauvegarde/json/etudiants_listes.json",
              "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4, ensure_ascii=False)

    with open("sauvegarde/json/etudiants_listes.json",
              "r", encoding="utf-8") as file:

        result = json.load(file)

    print(result)


# ==================================================
# 3. TUPLE - CSV
# ==================================================

def tuple_csv(data):

    print("\n--- TUPLE CSV ---")

    with open("sauvegarde/csv/etudiants_tuple.csv",
              "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["id", "nom", "age", "moyenne"])
        writer.writerows(data)

    with open("sauvegarde/csv/etudiants_tuple.csv",
              "r", encoding="utf-8") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)


# ==================================================
# 4. TUPLE - JSON
# ==================================================

def tuple_json(data):

    print("\n--- TUPLE JSON ---")

    with open("sauvegarde/json/etudiants_tuple.json",
              "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4, ensure_ascii=False)

    with open("sauvegarde/json/etudiants_tuple.json",
              "r", encoding="utf-8") as file:

        result = json.load(file)

    print(result)


# ==================================================
# 5. LIST OF DICTIONARIES - CSV
# ==================================================

def dict_csv(data):

    print("\n--- DICTIONARY CSV ---")

    with open("sauvegarde/csv/etudiants_dict.csv",
              "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=data[0].keys()
        )

        writer.writeheader()
        writer.writerows(data)

    with open("sauvegarde/csv/etudiants_dict.csv",
              "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


# ==================================================
# 6. LIST OF DICTIONARIES - JSON
# ==================================================

def dict_json(data):

    print("\n--- DICTIONARY JSON ---")

    with open("sauvegarde/json/etudiants_dict.json",
              "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4, ensure_ascii=False)

    with open("sauvegarde/json/etudiants_dict.json",
              "r", encoding="utf-8") as file:

        result = json.load(file)

    print(result)


# ==================================================
# 7. SET - CSV
# ==================================================

def set_csv(data):

    print("\n--- SET CSV ---")

    with open("sauvegarde/csv/competences.csv",
              "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["competence"])

        for competence in sorted(data):
            writer.writerow([competence])

    with open("sauvegarde/csv/competences.csv",
              "r", encoding="utf-8") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)


# ==================================================
# 8. SET - JSON
# ==================================================

def set_json(data):

    print("\n--- SET JSON ---")

    with open("sauvegarde/json/competences.json",
              "w", encoding="utf-8") as file:

        json.dump(sorted(data), file, indent=4, ensure_ascii=False)

    with open("sauvegarde/json/competences.json",
              "r", encoding="utf-8") as file:

        result = set(json.load(file))

    print(result)


# ==================================================
# 9. NESTED DICTIONARY - CSV
# ==================================================

def nested_dict_csv(data):

    print("\n--- NESTED DICTIONARY CSV ---")

    with open("sauvegarde/csv/registre_etudiants.csv",
              "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["id", "nom", "classe"])

        for student_id, info in data.items():

            writer.writerow([
                student_id,
                info["nom"],
                info["classe"]
            ])

    with open("sauvegarde/csv/registre_etudiants.csv",
              "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


# ==================================================
# 10. NESTED DICTIONARY - JSON
# ==================================================

def nested_dict_json(data):

    print("\n--- NESTED DICTIONARY JSON ---")

    with open("sauvegarde/json/registre_etudiants.json",
              "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4, ensure_ascii=False)

    with open("sauvegarde/json/registre_etudiants.json",
              "r", encoding="utf-8") as file:

        result = json.load(file)

    print(result)


# ==================================================
# 11. NAMEDTUPLE - CSV
# ==================================================

def namedtuple_csv(data):

    print("\n--- NAMEDTUPLE CSV ---")

    with open("sauvegarde/csv/etudiants_namedtuple.csv",
              "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(Etudiant._fields)

        for student in data:
            writer.writerow(student)

    with open("sauvegarde/csv/etudiants_namedtuple.csv",
              "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


# ==================================================
# 12. NAMEDTUPLE - JSON
# ==================================================

def namedtuple_json(data):

    print("\n--- NAMEDTUPLE JSON ---")

    students = [student._asdict() for student in data]

    with open("sauvegarde/json/etudiants_namedtuple.json",
              "w", encoding="utf-8") as file:

        json.dump(students, file, indent=4, ensure_ascii=False)

    with open("sauvegarde/json/etudiants_namedtuple.json",
              "r", encoding="utf-8") as file:

        result = json.load(file)

    restored = [
        Etudiant(**student)
        for student in result
    ]

    print(restored)


# ==================================================
# EXECUTION
# ==================================================

list_csv(etudiants_listes)
list_json(etudiants_listes)

tuple_csv(etudiants_tuple)
tuple_json(etudiants_tuple)

dict_csv(etudiants_dict)
dict_json(etudiants_dict)

set_csv(competences)
set_json(competences)

nested_dict_csv(registre_etudiants)
nested_dict_json(registre_etudiants)

namedtuple_csv(etudiants)
namedtuple_json(etudiants)


# ==================================================
# FIN
# ==================================================

print("\n===================================")
print("SAUVEGARDE TERMINEE AVEC SUCCES !")
print("===================================")

print("Fichiers CSV : sauvegarde/csv/")
print("Fichiers JSON : sauvegarde/json/")
