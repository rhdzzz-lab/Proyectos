import java.util.InputMismatchException;
import java.util.Scanner;

public class calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Hola, bienvenido a la calculadora simple.");
            System.out.println("Puedes realizar operaciones básicas entre dos números.");

            System.out.println("\nSelecciona la operación que deseas realizar:");
            System.out.println("1) Suma");
            System.out.println("2) Resta");
            System.out.println("3) Multiplicación");
            System.out.println("4) División");
            System.out.print("Opción: ");

            int opcion = scanner.nextInt();

            System.out.print("Ingresa el primer número: ");
            double num1 = scanner.nextDouble();

            System.out.print("Ingresa el segundo número: ");
            double num2 = scanner.nextDouble();

            double resultado;

            switch (opcion) {
                case 1:
                    resultado = num1 + num2;
                    System.out.println("Resultado de la suma: " + resultado);
                    break;
                case 2:
                    resultado = num1 - num2;
                    System.out.println("Resultado de la resta: " + resultado);
                    break;
                case 3:
                    resultado = num1 * num2;
                    System.out.println("Resultado de la multiplicación: " + resultado);
                    break;
                case 4:
                    if (num2 == 0) {
                        System.out.println("Error: No se puede dividir entre cero.");
                    } else {
                        resultado = num1 / num2;
                        System.out.println("Resultado de la división: " + resultado);
                    }
                    break;
                default:
                    System.out.println("Opción no válida. Debes elegir entre 1 y 4.");
            }
        } catch (InputMismatchException e) {
            System.out.println("Error: Debes ingresar un número válido.");
        } catch (Exception e) {
            System.out.println("Ocurrió un error inesperado: " + e.getMessage());
        } finally {
            scanner.close();
            System.out.println("Programa finalizado.");
        }
    }
}
