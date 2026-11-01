#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <typeinfo>

using namespace std;

// Helper function to simulate Python's divmod()
pair<int, int> divmod(int a, int b) {
    return make_pair(a / b, a % b);
}

int main() {
    // 1. Initializing collection elements (simulating array/list/tuple concepts)
    int numberArray[] = {1, 2, 4}; 
    vector<int> list_number = {1, 2, 4}; 

    // 2. User Input
    cout << "entrer un nombre = ";
    int input_number;
    if (!(cin >> input_number)) {
        cout << "Erreur de saisie." << endl;
        return 1;
    }

    // 3. Type conversions
    double float_input = (double)input_number;
    string string_number = to_string(input_number);

    // 4. Square root calculation (input_number ** 0.5)
    double square_input_number = sqrt(input_number);

    // 5. Look up element in the sequence
    auto it = find(list_number.begin(), list_number.end(), input_number);
    bool exists = (it != list_number.end());

    if (exists) {
        // Calculate vector index offset
        int index = distance(list_number.begin(), it);
        cout << "nombre existant " << input_number << ", indice " << index << endl;

        // 6. Verification of data types using typeid().name()
        cout << " du tuple, " << typeid(numberArray).name() << endl;
        cout << " du list, " << typeid(list_number).name() << endl;
        cout << " input_number, " << typeid(input_number).name() << endl;
        cout << " float input, " << typeid(float_input).name() << endl;
        cout << " string_number, " << typeid(string_number).name() << endl;
        cout << " square_input_number, " << typeid(square_input_number).name() << endl;

        // 7. Mathematical operations using the index
        cout << "somme = " << (input_number + index) << endl;
        cout << "substraction = " << (input_number - index) << endl;
        cout << "multiplication = " << (input_number * index) << endl;

        // Arithmetic protections against dividing by zero index
        if (index != 0) {
            cout << "division classic = " << ((double)input_number / index) << endl;
            cout << "division entiere = " << (input_number / index) << endl;
            cout << "division (modulo-reste) = " << (input_number % index) << endl;
            
            // Custom tuple display simulating divmod
            pair<int, int> dm = divmod(input_number, index);
            cout << "division = (" << dm.first << ", " << dm.second << ")" << endl;
        } else {
            cout << "Cannot divide by an index of 0!" << endl;
        }

    } else {
        cout << "nombre non existant essayer d'entrer un nombre dans la liste" << endl;
    }

    return 0;
}
