import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Sauvegarde {

    static Gson gson = new GsonBuilder()
            .setPrettyPrinting()
            .create();

    // Sauvegarde JSON
    public static void sauvegarderJSON(
            String nomFichier, Object donnees) throws IOException {

        Files.createDirectories(Paths.get("sauvegrade/json"));

        String chemin = "sauvegrade/json/" + nomFichier + ".json";

        try (Writer writer = new FileWriter(chemin)) {
            gson.toJson(donnees, writer);
        }

        System.out.println("JSON sauvegardé : " + chemin);
    }

    // Sauvegarde CSV
    public static void sauvegarderCSV(
            String nomFichier,
            String contenu) throws IOException {

        Files.createDirectories(Paths.get("sauvegrade/csv"));

        String chemin = "sauvegrade/csv/" + nomFichier + ".csv";

        try (Writer writer = new FileWriter(chemin)) {
            writer.write(contenu);
        }

        System.out.println("CSV sauvegardé : " + chemin);
    }
}