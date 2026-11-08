#include <iostream>
#include "data.h"

using namespace std;

int day4_ex() {

    // Access the SAME existing data
    cout << etudiants_dict[0].nom << endl;

    cout << etudiant_tuple.nom << endl;

    cout << competences[0] << endl;

    cout << registre[0].nom << endl;

    cout << date_inscription.annee << endl;

    cout << etudiant_1.nom << endl;

    return 0;
}