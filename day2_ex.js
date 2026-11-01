
import fs from "node:fs";


// Declaration des variables
const startupNumbers = [1, 2, 3];

console.log("Entrer un nombre :");
const inputNumber = Number(fs.readFileSync(0, "utf-8").trim()); 

const listNumber = [...startupNumbers];
const floatInput = parseFloat(inputNumber);
const stringNumber = String(inputNumber);
const squareInputNumber = inputNumber ** 0.5;


// 1. Verification d'existence
function existenceVerification(inputNumber) {

    if (startupNumbers.includes(inputNumber)) {

        console.log(
            `Nombre existant : ${inputNumber}, indice : ${startupNumbers.indexOf(inputNumber)}`
        );

    } else {

        console.log(
            `Nombre introuvable. Valeurs autorisees : ${startupNumbers}`
        );

    }
}


// 2. Verification des types
function verificationType() {

    console.log("\n--- VERIFICATION DES TYPES ---");

    console.log("Type du tableau :", Array.isArray(startupNumbers) ? "Array" : typeof startupNumbers);
    console.log("Type de la liste :", Array.isArray(listNumber) ? "Array" : typeof listNumber);
    console.log("Type inputNumber :", typeof inputNumber);
    console.log("Type floatInput :", typeof floatInput);
    console.log("Type stringNumber :", typeof stringNumber);
    console.log("Type squareInputNumber :", typeof squareInputNumber);

}

console.log("Entrer la taille du tableau :");

// 3. Creation automatique d'un tableau
const inputArraySize = Number(fs.readFileSync(0, "utf-8").trim()); 

const inputNumbers = [];

function arrayListHandle() {

    for (let i = 1; i <= inputArraySize; i++) {
        console.log(`Entrer le nombre ${i} :`)

        const number = Number(fs.readFileSync(0, "utf-8").trim()); 

        inputNumbers.push(number);

        console.log("List :", inputNumbers);

        console.log(
            `Number ${number}, indice : ${inputNumbers.indexOf(number)}`
        );

    }

}


// 4. Operations mathematiques
function calculate(a, b) {

    console.log("\n--- OPERATIONS MATHEMATIQUES ---");

    console.log(`Somme = ${a + b}`);
    console.log(`Soustraction = ${a - b}`);
    console.log(`Multiplication = ${a * b}`);

    if (b !== 0) {

        console.log(`Division classique = ${a / b}`);
        console.log(`Division entiere = ${Math.trunc(a / b)}`);
        console.log(`Modulo = ${a % b}`);

        console.log(
            `Divmod = (${Math.trunc(a / b)}, ${a % b})`
        );

    } else {

        console.log("Division impossible : division par zero.");

    }

}


// 5. Appel des fonctions
existenceVerification(inputNumber);

verificationType();

arrayListHandle();

if (startupNumbers.includes(inputNumber)) {

    calculate(inputNumber, startupNumbers.indexOf(inputNumber));

}
