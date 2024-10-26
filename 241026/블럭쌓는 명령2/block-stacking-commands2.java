import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] blocks = new int[n];

        for (int i = 0; i < k; i++) {
            int first = sc.nextInt();
            int second = sc.nextInt();

            for (int j = first; j <= second; j++) {
                blocks[j] += 1;
            }
        }

        int maxVal = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (maxVal < blocks[i]) {
                maxVal = blocks[i];
            }
        }
    
        System.out.println(maxVal);
    }
}