import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += sc.nextDouble();
        }

        double average = (double)sum / n;
        System.out.printf("%.1f\n", average);
        if (average >= 4.0) {
            System.out.println("Perfect");
        } else if (average >= 3.0) {
            System.out.println("Good");
        } else {
            System.out.println("Poor");
        }
    }
}