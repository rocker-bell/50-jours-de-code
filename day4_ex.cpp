#include <iostream>
#include "data.h"

using namespace std;

int main() {

    cout << "========== DAY 4 ==========" << endl;

    cout << "\n--- DICTIONARY ---" << endl;
    cout << etudiants_dict[0].nom << endl;

    cout << "\n--- TUPLE ---" << endl;
    cout << etudiant_tuple.nom << endl;

    cout << "\n--- COMPETENCES ---" << endl;
    for (int i = 0; i < 4; i++) {
        cout << competences[i] << endl;
    }

    cout << "\n--- REGISTRE ---" << endl;
    for (int i = 0; i < 3; i++) {
        cout << registre[i].code << " "
             << registre[i].nom << " "
             << registre[i].classe << endl;
    }

    cout << "\n--- DATE ---" << endl;
    cout << date_inscription.annee << "/"
         << date_inscription.mois << "/"
         << date_inscription.jour << endl;

    cout << "\n--- NAMED STRUCT ---" << endl;
    cout << etudiant_1.nom << endl;

    cout << "\n===========================" << endl;

    return 0;
}