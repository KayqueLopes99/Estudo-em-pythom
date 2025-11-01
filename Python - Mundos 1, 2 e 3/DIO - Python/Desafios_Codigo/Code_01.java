
import java.util.Scanner;

public class Code_01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Brute Salary: ");
        double BruteSalary = scanner.nextDouble();

        System.out.print("Enter Additional Benefit: ");
        double aditionalBenefit = scanner.nextDouble();

        double percentImpost = 0;
        if ((BruteSalary <= 0.0) && (BruteSalary <= 1100.0)) {
            percentImpost = 0.05 * BruteSalary;

        } else if ((BruteSalary > 1100.0) && (BruteSalary <= 2500.0)) {
            percentImpost = 0.1 * BruteSalary;

        } else if (BruteSalary > 2500.0) {
            percentImpost = 0.15 * BruteSalary;
            
        } else {
            percentImpost = 0.0;
        }

        double salaryTransport = (BruteSalary - percentImpost) + aditionalBenefit;

        System.out.printf("Salary Transport: %.2f%n", salaryTransport);

        scanner.close();
    }
}