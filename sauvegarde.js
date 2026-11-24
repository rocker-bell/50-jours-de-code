
const fs = require('fs');
const path = require('path');

class Sauvegarde {

    // Sauvegarde JSON
    static sauvegarderJSON(nomFichier, donnees) {

        // Créer le dossier s'il n'existe pas
        const dossier = 'sauvegrade/json';

        fs.mkdirSync(dossier, { recursive: true });

        // Construire le chemin
        const chemin = path.join(
            dossier,
            nomFichier + '.json'
        );

        // Convertir les données en JSON
        const contenu = JSON.stringify(donnees, null, 4);

        // Écrire dans le fichier
        fs.writeFileSync(chemin, contenu, 'utf8');

        console.log('JSON sauvegardé : ' + chemin);
    }


    // Sauvegarde CSV
    static sauvegarderCSV(nomFichier, donnees) {

        // Créer le dossier s'il n'existe pas
        const dossier = 'sauvegrade/csv';

        fs.mkdirSync(dossier, { recursive: true });

        // Construire le chemin
        const chemin = path.join(
            dossier,
            nomFichier + '.csv'
        );

        // Transformer les données en texte CSV
        const contenu = donnees.map(ligne =>
            ligne.map(valeur => {
                const texte = String(valeur ?? '');
                return '"' + texte.replace(/"/g, '""') + '"';
            }).join(',')
        ).join('\n');

        // Écrire dans le fichier
        fs.writeFileSync(chemin, contenu, 'utf8');

        console.log('CSV sauvegardé : ' + chemin);
    }

}
 
module.exports = Sauvegarde;