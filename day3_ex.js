
// 1. Array of objects (equivalent to Python dictionaries)
const etudiants_dict = [
    { id: 1, nom: "Amina", age: 20, moyenne_generale: 15.5 },
    { id: 2, nom: "Youssef", age: 22, moyenne_generale: 13.8 },
    { id: 3, nom: "Sofia", age: 21, moyenne_generale: 16.2 },
    { id: 4, nom: "Amine", age: 23, moyenne_generale: 11.4 }
];

// Loop through students
function etudiants_dict_loop(etudiants_dict) {

    etudiants_dict.forEach((etudiant, index) => {

        if (etudiant.id === 1) {
            console.log("Dictionnaire :", etudiant);
        }

        // Loop through object properties
        for (const [key, value] of Object.entries(etudiant)) {
            console.log(`key : ${key} and value : ${value}`);
        }

        console.log("dict :", etudiant, "index :", index);
    });
}

etudiants_dict_loop(etudiants_dict);


// 2. List of lists (Array of Arrays)
const etudiants_listes = [
    [1, "Amina", 20, 15.5],
    [2, "Youssef", 22, 13.8],
    [3, "Sofia", 21, 16.2],
    [4, "Amine", 23, 11.4]
];


// 3. Tuple equivalent: frozen arrays
const etudiants_tuple = Object.freeze([
    Object.freeze([1, "Amina", 20, 15.5]),
    Object.freeze([2, "Youssef", 22, 13.8]),
    Object.freeze([3, "Sofia", 21, 16.2]),
    Object.freeze([4, "Amine", 23, 11.4])
]);


// 4. Set: automatically removes duplicates
const competences = new Set([
    "Python", "SQL", "Git", "Python", "Excel"
]);

console.log(competences);


// 5. Nested objects (equivalent to nested dictionaries)
const registre_etudiants = {
    "ETUD-001": { nom: "Amina", classe: "A" },
    "ETUD-002": { nom: "Youssef", classe: "B" },
    "ETUD-003": { nom: "Sofia", classe: "A" }
};

console.log(registre_etudiants["ETUD-003"].nom);


// 6. Date
// JavaScript months start at 0: September = 8
const date_inscription = new Date(2026, 8, 1);

const formattedDate = date_inscription.toLocaleDateString("en-GB");

console.log("Inscrit le :", formattedDate);


// 7. Namedtuple equivalent: class
class Etudiant {
    constructor(id, nom, moyenne) {
        this.id = id;
        this.nom = nom;
        this.moyenne = moyenne;

        Object.freeze(this);
    }
}

const etudiant_1 = new Etudiant(10, "Amine", 14.5);

console.log(etudiant_1.nom);
console.log(etudiant_1.moyenne);
