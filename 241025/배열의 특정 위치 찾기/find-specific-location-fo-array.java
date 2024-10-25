import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
        }

        int sum = 0;
        int sum3 = 0;
        int cnt = 0;
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                sum += arr[i - 1];
            }
            if (i % 3 == 0) {
                sum3 += arr[i - 1];
                cnt += 1;
            }
        }

        double average = (double)sum3 / cnt;

        System.out.printf("%d %.1f", sum, average);
    }
}