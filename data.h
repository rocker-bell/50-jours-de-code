#ifndef DATA_H
#define DATA_H

#include <string>
using namespace std;

// Structures
struct Etudiant {
    int id;
    string nom;
    int age;
    float moyenne_generale;
};

struct Registre {
    string code;
    string nom;
    char classe;
};

struct Date {
    int annee, mois, jour;
};

struct EtudiantNamed {
    int id;
    string nom;
    float moyenne;
};

// Declare existing variables
extern Etudiant etudiants_dict[4];
extern float etudiants_listes[4][4];
extern Etudiant etudiant_tuple;
extern string competences[4];
extern Registre registre[3];
extern Date date_inscription;
extern EtudiantNamed etudiant_1;

#endif