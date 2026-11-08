#include "data.h"

// Actual shared data
Etudiant etudiants_dict[] = {
    {1, "Amina", 20, 15.5},
    {2, "Youssef", 22, 13.8},
    {3, "Sofia", 21, 16.2},
    {4, "Amine", 23, 11.4}
};

float etudiants_listes[4][4] = {
    {1, 20, 15.5, 0},
    {2, 22, 13.8, 0},
    {3, 21, 16.2, 0},
    {4, 23, 11.4, 0}
};

Etudiant etudiant_tuple = {1, "Amina", 20, 15.5};

string competences[] = {"Python", "SQL", "Git", "Excel"};

Registre registre[] = {
    {"ETUD-001", "Amina", 'A'},
    {"ETUD-002", "Youssef", 'B'},
    {"ETUD-003", "Sofia", 'A'}
};

Date date_inscription = {2026, 9, 1};

EtudiantNamed etudiant_1 = {10, "Amine", 14.5};