
#include <iostream>
#include <fstream>
#include <filesystem>
#include <algorithm>
#include <nlohmann/json.hpp>

#include "data.h"

using namespace std;
using namespace filesystem;
using json = nlohmann::json;


// ==================================================
// CREATION DES DOSSIERS
// ==================================================

void creer_dossiers() {

    create_directories("sauvegarde/csv");
    create_directories("sauvegarde/json");

    cout << "Dossiers crees avec succes !" << endl;
}


// ==================================================
// 1. LIST OF LISTS - CSV
// ==================================================

void list_csv() {

    ofstream file("sauvegarde/csv/etudiants_listes.csv");

    file << "id,nom,age,moyenne\n";

    for (int i = 0; i < 4; i++) {

        file << etudiants_listes[i][0] << ","
             << etudiants_dict[i].nom << ","
             << etudiants_listes[i][1] << ","
             << etudiants_listes[i][2] << "\n";
    }

    file.close();
}


// ==================================================
// 2. LIST OF LISTS - JSON
// ==================================================

void list_json() {

    json data = json::array();

    for (int i = 0; i < 4; i++) {

        data.push_back({
            {"id", etudiants_listes[i][0]},
            {"nom", etudiants_dict[i].nom},
            {"age", etudiants_listes[i][1]},
            {"moyenne", etudiants_listes[i][2]}
        });
    }

    ofstream file("sauvegarde/json/etudiants_listes.json");

    file << data.dump(4);

    file.close();
}


// ==================================================
// 3. TUPLE - CSV
// ==================================================

void tuple_csv() {

    ofstream file("sauvegarde/csv/etudiants_tuple.csv");

    file << "id,nom,age,moyenne\n";

    file << etudiant_tuple.id << ","
         << etudiant_tuple.nom << ","
         << etudiant_tuple.age << ","
         << etudiant_tuple.moyenne_generale << "\n";

    file.close();
}


// ==================================================
// 4. TUPLE - JSON
// ==================================================

void tuple_json() {

    json data = {
        {"id", etudiant_tuple.id},
        {"nom", etudiant_tuple.nom},
        {"age", etudiant_tuple.age},
        {"moyenne", etudiant_tuple.moyenne_generale}
    };

    ofstream file("sauvegarde/json/etudiants_tuple.json");

    file << data.dump(4);

    file.close();
}


// ==================================================
// 5. DICTIONARY - CSV
// ==================================================

void dict_csv() {

    ofstream file("sauvegarde/csv/etudiants_dict.csv");

    file << "id,nom,age,moyenne\n";

    for (const auto& e : etudiants_dict) {

        file << e.id << ","
             << e.nom << ","
             << e.age << ","
             << e.moyenne_generale << "\n";
    }

    file.close();
}


// ==================================================
// 6. DICTIONARY - JSON
// ==================================================

void dict_json() {

    json data = json::array();

    for (const auto& e : etudiants_dict) {

        data.push_back({
            {"id", e.id},
            {"nom", e.nom},
            {"age", e.age},
            {"moyenne", e.moyenne_generale}
        });
    }

    ofstream file("sauvegarde/json/etudiants_dict.json");

    file << data.dump(4);

    file.close();
}


// ==================================================
// 7. SET - CSV
// ==================================================

void set_csv() {

    ofstream file("sauvegarde/csv/competences.csv");

    file << "competence\n";

    string temp[4];

    copy(competences, competences + 4, temp);

    sort(temp, temp + 4);

    for (const auto& c : temp) {

        file << c << "\n";
    }

    file.close();
}


// ==================================================
// 8. SET - JSON
// ==================================================

void set_json() {

    string temp[4];

    copy(competences, competences + 4, temp);

    sort(temp, temp + 4);

    json data = json::array();

    for (const auto& c : temp) {

        data.push_back(c);
    }

    ofstream file("sauvegarde/json/competences.json");

    file << data.dump(4);

    file.close();
}


// ==================================================
// 9. NESTED DICTIONARY - CSV
// ==================================================

void nested_dict_csv() {

    ofstream file("sauvegarde/csv/registre_etudiants.csv");

    file << "id,nom,classe\n";

    for (const auto& r : registre) {

        file << r.code << ","
             << r.nom << ","
             << r.classe << "\n";
    }

    file.close();
}


// ==================================================
// 10. NESTED DICTIONARY - JSON
// ==================================================

void nested_dict_json() {

    json data = json::array();

    for (const auto& r : registre) {

        data.push_back({
            {"id", r.code},
            {"nom", r.nom},
            {"classe", string(1, r.classe)}
        });
    }

    ofstream file("sauvegarde/json/registre_etudiants.json");

    file << data.dump(4);

    file.close();
}


// ==================================================
// 11. NAMED STRUCT - CSV
// ==================================================

void namedtuple_csv() {

    ofstream file("sauvegarde/csv/etudiants_namedtuple.csv");

    file << "id,nom,moyenne\n";

    file << etudiant_1.id << ","
         << etudiant_1.nom << ","
         << etudiant_1.moyenne << "\n";

    file.close();
}


// ==================================================
// 12. NAMED STRUCT - JSON
// ==================================================

void namedtuple_json() {

    json data = {
        {"id", etudiant_1.id},
        {"nom", etudiant_1.nom},
        {"moyenne", etudiant_1.moyenne}
    };

    ofstream file("sauvegarde/json/etudiants_namedtuple.json");

    file << data.dump(4);

    file.close();
}


// ==================================================
// EXECUTION
// ==================================================

int main() {

    creer_dossiers();

    list_csv();
    list_json();

    tuple_csv();
    tuple_json();

    dict_csv();
    dict_json();

    set_csv();
    set_json();

    nested_dict_csv();
    nested_dict_json();

    namedtuple_csv();
    namedtuple_json();

    cout << "\n====================================" << endl;
    cout << "SAUVEGARDE TERMINEE AVEC SUCCES !" << endl;
    cout << "====================================" << endl;

    cout << "CSV  : sauvegarde/csv/" << endl;
    cout << "JSON : sauvegarde/json/" << endl;

    return 0;
}
