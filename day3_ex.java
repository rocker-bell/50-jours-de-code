
import java.util.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class day3_ex {

    // 1. Student class (equivalent to dictionary)
    static class Etudiant {
        int id;
        String nom;
        int age;
        double moyenne_generale;

        Etudiant(int id, String nom, int age, double moyenne) {
            this.id = id;
            this.nom = nom;
            this.age = age;
            this.moyenne_generale = moyenne;
        }

        public String toString() {
            return "id=" + id + ", nom=" + nom +
                   ", age=" + age + ", moyenne=" + moyenne_generale;
        }
    }

    public static void main(String[] args) {

        // 1. List of student objects
        List<Etudiant> etudiants_dict = new ArrayList<>();

        etudiants_dict.add(new Etudiant(1, "Amina", 20, 15.5));
        etudiants_dict.add(new Etudiant(2, "Youssef", 22, 13.8));
        etudiants_dict.add(new Etudiant(3, "Sofia", 21, 16.2));
        etudiants_dict.add(new Etudiant(4, "Amine", 23, 11.4));

        // Loop
        for (int i = 0; i < etudiants_dict.size(); i++) {
            Etudiant e = etudiants_dict.get(i);

            if (e.id == 1) {
                System.out.println("Dictionnaire : " + e);
            }

            System.out.println("Index : " + i);
        }

        // 2. List of lists
        List<List<Object>> etudiants_listes = new ArrayList<>();

        etudiants_listes.add(Arrays.asList(1, "Amina", 20, 15.5));
        etudiants_listes.add(Arrays.asList(2, "Youssef", 22, 13.8));
        etudiants_listes.add(Arrays.asList(3, "Sofia", 21, 16.2));
        etudiants_listes.add(Arrays.asList(4, "Amine", 23, 11.4));

        // 3. Tuple equivalent: immutable List
        List<Object> etudiants_tuple =
            Collections.unmodifiableList(
                Arrays.asList(1, "Amina", 20, 15.5)
            );

        // 4. Set: automatically removes duplicates
        Set<String> competences = new HashSet<>(
            Arrays.asList("Python", "SQL", "Git", "Python", "Excel")
        );

        System.out.println(competences);

        // 5. Nested HashMap
        Map<String, Map<String, String>> registre_etudiants =
            new HashMap<>();

        registre_etudiants.put("ETUD-001",
            Map.of("nom", "Amina", "classe", "A"));

        registre_etudiants.put("ETUD-002",
            Map.of("nom", "Youssef", "classe", "B"));

        registre_etudiants.put("ETUD-003",
            Map.of("nom", "Sofia", "classe", "A"));

        System.out.println(
            registre_etudiants.get("ETUD-003").get("nom")
        );

        // 6. Date
        LocalDate date_inscription = LocalDate.of(2026, 9, 1);

        DateTimeFormatter formatter =
            DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println(
            "Inscrit le : " + date_inscription.format(formatter)
        );

        // 7. Namedtuple equivalent: immutable record
        record EtudiantRecord(int id, String nom, double moyenne) {}

        EtudiantRecord etudiant_1 =
            new EtudiantRecord(10, "Amine", 14.5);

        System.out.println(etudiant_1.nom());
        System.out.println(etudiant_1.moyenne());
    }
}
