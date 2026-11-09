
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class day2_ex {

    // Ensemble initial
    static ArrayList<Integer> startup_numbers =
            new ArrayList<>(Arrays.asList(1, 2, 3));

    static ArrayList<Integer> list_number =
            new ArrayList<>(startup_numbers);

    static ArrayList<Integer> input_numbers =
            new ArrayList<>();

    static int input_number;
    static double float_input;
    static String string_number;
    static double square_input_number;

    static Scanner scanner = new Scanner(System.in);

    // Verification d'existence
    static int existence_verification(int number) {

        if (startup_numbers.contains(number)) {

            int index = startup_numbers.indexOf(number);

            System.out.println(
                "Nombre existant " + number +
                ", indice " + index
            );

            return index;

        } else {

            System.out.println(
                "Nombre introuvable. Entrez un nombre dans l'ensemble : "
                + startup_numbers
            );

            return -1;
        }
    }

    // Verification des types
    static void verification_type() {

        System.out.println("\n--- VERIFICATION DES TYPES ---");

        System.out.println("Type de la liste : "
                + startup_numbers.getClass().getSimpleName());

        System.out.println("Type de list_number : "
                + list_number.getClass().getSimpleName());

        System.out.println("Type input_number : int");

        System.out.println("Type float_input : double");

        System.out.println("Type string_number : String");

        System.out.println("Type square_input_number : double");
    }

    // Creation automatique de la liste
    static void array_list_handle(int size) {

        for (int i = 1; i <= size; i++) {

            System.out.print(
                "Entrer le nombre " + i + " de la liste = "
            );

            int number = scanner.nextInt();

            input_numbers.add(number);

            System.out.println("List : " + input_numbers);

            System.out.println(
                "Number " + number +
                " indice : " + (input_numbers.size() - 1)
            );
        }
    }

    // Operations mathematiques
    static void calculate(double a, double b) {

        System.out.println("\n--- OPERATIONS MATHEMATIQUES ---");

        System.out.println("Somme = " + (a + b));

        System.out.println("Soustraction = " + (a - b));

        System.out.println("Multiplication = " + (a * b));

        if (b != 0) {

            System.out.println("Division classique = " + (a / b));

            System.out.println("Division entiere = "
                    + (int)(a / b));

            System.out.println("Modulo = " + (a % b));

            System.out.println("Divmod = "
                    + (Math.floorDiv((int)a, (int)b))
                    + ", " + (a % b));

        } else {

            System.out.println(
                "Division impossible : division par zero."
            );
        }
    }

    // Programme principal
    public static void main(String[] args) {

        System.out.print("Entrer un nombre valide = ");

        input_number = scanner.nextInt();

        float_input = (double) input_number;

        string_number = String.valueOf(input_number);

        square_input_number = Math.sqrt(input_number);

        int index = existence_verification(input_number);

        verification_type();

        System.out.print("\nEntrer la taille de la liste = ");

        int input_array_size = scanner.nextInt();

        array_list_handle(input_array_size);

        if (index != -1) {
            calculate(input_number, index);
        }

        scanner.close();
    }
}
