import java.util.Scanner;

public class AdditionWithScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompting the user to enter the first number
        System.out.print("Enter the first number: ");
        double firstNumber = scanner.nextDouble();

        // Prompting the user to enter the second number
        System.out.print("Enter the second number: ");
        double secondNumber = scanner.nextDouble();

        // Adding the two numbers
        double sum = firstNumber + secondNumber;

        // Displaying the result
        System.out.println("The sum of " + firstNumber + " and " + secondNumber + " is: " + sum);

<<<<<<< HEAD
        // Displaying the result
        System.out.println("The sum of " + firstNumber + " and " + secondNumber + " is: " + sum);

=======
>>>>>>> eef8119d22143ff04b78eadf18932a6a06680aa7
        scanner.close(); // Closing the scanner to prevent resource leak
    }
}
