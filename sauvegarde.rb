
require 'json'
require 'csv'
require 'fileutils'

class Sauvegarde

  # Sauvegarde JSON
  def self.sauvegarder_json(nom_fichier, donnees)

    # Créer le dossier s'il n'existe pas
    FileUtils.mkdir_p('sauvegrade/json')

    # Construire le chemin
    chemin = "sauvegrade/json/#{nom_fichier}.json"

    # Convertir les données en JSON et sauvegarder
    File.write(chemin, JSON.pretty_generate(donnees))

    puts "JSON sauvegardé : #{chemin}"
  end

  # Sauvegarde CSV
  def self.sauvegarder_csv(nom_fichier, donnees)

    # Créer le dossier s'il n'existe pas
    FileUtils.mkdir_p('sauvegrade/csv')

    # Construire le chemin
    chemin = "sauvegrade/csv/#{nom_fichier}.csv"

    # Écrire les données dans le fichier CSV
    CSV.open(chemin, 'w') do |csv|
      donnees.each do |ligne|
        csv << ligne
      end
    end

    puts "CSV sauvegardé : #{chemin}"
  end

end
