
// Cet exercice envisage plusieurs utilisations des types de données
// de base et les interactions entre eux.

import fs from "node:fs";

// Tuple simulé (JavaScript ne possède pas de tuple natif)
const number = Object.freeze([1, 3, 5]);

// Transformation du tuple en tableau modifiable
const list_number = Array.from(number);

// Saisie utilisateur
console.log("Entrer un nombre :");

let input_number = Number(fs.readFileSync(0, "utf-8").trim()); 
// enter + (ctl  z)
// Conversion des types
let float_input = Number(input_number);
let string_number = String(input_number);

// Calcul de la racine carrée
let square_input_number = input_number ** 0.5;

// Vérification de l'existence du nombre
if (number.includes(input_number)) {
    console.log(
        `Nombre existant ${input_number}, indice ${number.indexOf(input_number)}`
    );
} else {
    console.log(
        `Nombre ${input_number} non existant dans la liste : ${list_number}`
    );
}

// Affichage des types
console.log(`Type du tuple : ${typeof number}`);
console.log(`Type du list : ${typeof list_number}`);
console.log(`Type input_number : ${typeof input_number}`);
console.log(`Type float_input : ${typeof float_input}`);
console.log(`Type string_number : ${typeof string_number}`);
console.log(`Type square_input_number : ${typeof square_input_number}`);
