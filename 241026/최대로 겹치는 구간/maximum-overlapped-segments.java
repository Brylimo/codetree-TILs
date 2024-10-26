import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        final int OFFSET = 100;

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] line = new int[201];

        for (int i = 0; i < n; i++) {
            int x1 = sc.nextInt();
            int x2 = sc.nextInt();

            for (int j = x1; j <= x2; j++) {
                line[j] += 1;
            }
        }

        int maxVal = Integer.MIN_VALUE;
        for (int i = 0; i < 201; i++) {
            if (maxVal < line[i]) {
                maxVal = line[i];
            }
        }

        System.out.println(maxVal);
    }
}