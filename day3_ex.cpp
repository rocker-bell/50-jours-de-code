
#include <iostream>
#include <iomanip>
using namespace std;

// 1. Student structure
struct Etudiant {
    int id;
    string nom;
    int age;
    float moyenne_generale;
};

Etudiant etudiants_dict[] = {
    {1, "Amina", 20, 15.5},
    {2, "Youssef", 22, 13.8},
    {3, "Sofia", 21, 16.2},
    {4, "Amine", 23, 11.4}
};

// 2. List of lists equivalent
float etudiants_listes[4][4] = {
    {1, 20, 15.5, 0},
    {2, 22, 13.8, 0},
    {3, 21, 16.2, 0},
    {4, 23, 11.4, 0}
};

// 3. Tuple equivalent
Etudiant etudiant_tuple = {1, "Amina", 20, 15.5};

// 4. Set equivalent
string competences[] = {"Python", "SQL", "Git", "Excel"};

// 5. Nested dictionary equivalent
struct Registre {
    string code;
    string nom;
    char classe;
};

Registre registre[] = {
    {"ETUD-001", "Amina", 'A'},
    {"ETUD-002", "Youssef", 'B'},
    {"ETUD-003", "Sofia", 'A'}
};

// 6. Date equivalent
struct Date {
    int annee, mois, jour;
};

Date date_inscription = {2026, 9, 1};

// 7. Namedtuple equivalent
struct EtudiantNamed {
    int id;
    string nom;
    float moyenne;
};

EtudiantNamed etudiant_1 = {10, "Amine", 14.5};

// Print functions
void print_etudiants_dict() {
    for (int i = 0; i < 4; i++) {
        if (etudiants_dict[i].id == 1) {
            cout << "Dictionnaire : "
                 << etudiants_dict[i].id << ", "
                 << etudiants_dict[i].nom << ", "
                 << etudiants_dict[i].age << ", "
                 << fixed << setprecision(1)
                 << etudiants_dict[i].moyenne_generale << endl;
        }

        cout << "Index : " << i << endl;
    }
}

void print_etudiant_listes() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << etudiants_listes[i][j] << " ";
        }
        cout << endl;
    }
}

void print_tuple() {
    cout << etudiant_tuple.id << ", "
         << etudiant_tuple.nom << ", "
         << etudiant_tuple.age << ", "
         << etudiant_tuple.moyenne_generale << endl;
}

void print_competences() {
    for (string competence : competences) {
        cout << competence << endl;
    }
}

void print_registre() {
    cout << "Etudiant : " << registre[2].nom << endl;
}

void print_date() {
    cout << "Inscrit le : "
         << setfill('0') << setw(2) << date_inscription.jour << "/"
         << setw(2) << date_inscription.mois << "/"
         << setw(4) << date_inscription.annee << endl;
}

void print_namedtuple() {
    cout << etudiant_1.nom << " : "
         << fixed << setprecision(1)
         << etudiant_1.moyenne << endl;
}

// MAIN: print calls only
int main() {
    print_etudiants_dict();
    print_etudiant_listes();
    print_tuple();
    print_competences();
    print_registre();
    print_date();
    print_namedtuple();

    return 0;
}
