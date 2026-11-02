
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <typeinfo>

using namespace std;

// Ensemble initial
vector<int> startup_numbers = {1, 2, 3};

vector<int> list_number = startup_numbers;

int input_number;
double float_input;
string string_number;
double square_input_number;

vector<int> input_numbers;

// Verification d'existence
int existence_verification(int number) {
    for (int i = 0; i < startup_numbers.size(); i++) {
        if (startup_numbers[i] == number) {
            cout << "Nombre existant " << number
                 << ", indice " << i << endl;
            return i;
        }
    }

    cout << "Nombre introuvable. Entrez un nombre dans l'ensemble : ";

    for (int n : startup_numbers) {
        cout << n << " ";
    }

    cout << endl;
    return -1;
}

// Verification des types
void verification_type() {
    cout << "\n--- VERIFICATION DES TYPES ---\n";

    cout << "Type du vector : vector<int>" << endl;
    cout << "Type du nombre : int" << endl;
    cout << "Type float_input : double" << endl;
    cout << "Type string_number : string" << endl;
    cout << "Type square_input_number : double" << endl;
}

// Creation automatique de la liste
void array_list_handle(int size) {
    for (int i = 1; i <= size; i++) {
        int number;

        cout << "Entrer le nombre " << i << " de la liste = ";
        cin >> number;

        input_numbers.push_back(number);

        cout << "List : ";

        for (int n : input_numbers) {
            cout << n << " ";
        }

        cout << endl;

        cout << "Number " << number
             << " indice : "
             << input_numbers.size() - 1 << endl;
    }
}

// Operations mathematiques
void calculate(double a, double b) {
    cout << "\n--- OPERATIONS MATHEMATIQUES ---\n";

    cout << "Somme = " << a + b << endl;
    cout << "Soustraction = " << a - b << endl;
    cout << "Multiplication = " << a * b << endl;

    if (b != 0) {
        cout << "Division classique = " << a / b << endl;
        cout << "Division entiere = " << (int)(a / b) << endl;
        cout << "Modulo = " << fmod(a, b) << endl;
    } else {
        cout << "Division impossible : division par zero." << endl;
    }
}

// Programme principal
int main() {

    cout << "Entrer un nombre valide = ";
    cin >> input_number;

    float_input = (double)input_number;
    string_number = to_string(input_number);
    square_input_number = sqrt(input_number);

    int index = existence_verification(input_number);

    verification_type();

    int input_array_size;

    cout << "\nEntrer la taille de la liste = ";
    cin >> input_array_size;

    array_list_handle(input_array_size);

    if (index != -1) {
        calculate(input_number, index);
    }

    return 0;
}
