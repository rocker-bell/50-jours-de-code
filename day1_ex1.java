import java.util.Scanner;
import java.util.Arrays;
import java.util.List;

public class day1_ex1 {

    public static void main(String[] args) {
        // Initialize Scanner for user input
        Scanner scanner = new Scanner(System.in);

        // Arrays/Lists for type verification matching your print statements
        Integer[] numberTuple = {1, 2, 4}; // Represents the 'tuple'
        List<Integer> list_number = Arrays.asList(numberTuple); // Represents the 'list'

        System.out.print("entrer un nombre = ");
        int input_number = scanner.nextInt();

        // Type conversions
        double float_input = (double) input_number; // Java uses double/float for decimals
        String string_number = String.valueOf(input_number);

        // Square root calculation (input_number ** 0.5)
        double square_input_number = Math.sqrt(input_number);

        // Check if the number exists in the array
        boolean exists = Arrays.stream(numberTuple).anyMatch(x -> x == input_number);

        if (exists) {
            // Find the index of the number
            int index = list_number.indexOf(input_number);
            System.out.println("nombre existant " + input_number + ", indice " + index);

            // Verification of data types using .getClass().getSimpleName()
            System.out.println(" du tuple, " + numberTuple.getClass().getSimpleName());
            System.out.println(" du list, " + list_number.getClass().getSimpleName());
            System.out.println(" input_number, " + ((Object) input_number).getClass().getSimpleName());
            System.out.println(" float input, " + ((Object) float_input).getClass().getSimpleName());
            System.out.println(" string_number, " + string_number.getClass().getSimpleName());
            System.out.println(" square_input_number, " + ((Object) square_input_number).getClass().getSimpleName());

            // Mathematical operations using the index
            System.out.println("somme = " + (input_number + index));
            System.out.println("substraction = " + (input_number - index));
            System.out.println("multiplication = " + (input_number * index));

            // Arithmetic checks to avoid division by zero if index is 0
            if (index != 0) {
                System.out.println("division classic = " + ((double) input_number / index));
                System.out.println("division entiere = " + (input_number / index));
                System.out.println("division (modulo-reste) = " + (input_number % index));
                System.out.println("division = (" + (input_number / index) + ", " + (input_number % index) + ")"); // Emulates divmod()
            } else {
                System.out.println("Cannot divide by an index of 0!");
            }

        } else {
            System.out.println("nombre non existant essayer d'entrer un nombre dans la liste");
        }

        scanner.close(); // Clean up scanner resource
    }
}
