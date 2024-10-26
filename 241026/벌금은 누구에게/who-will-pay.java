import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();

        int[] penalty = new int[n + 1];

        for (int i = 0; i < n; i++) {
            penalty[i] = k;
        }
    
        int ans = -1;
        for (int i = 0; i < m; i++) {
            int num = sc.nextInt();

            penalty[num] -= 1;

            if (penalty[num] == 0) {
                ans = num;
                break;
            }
        }

        System.out.println(ans);
    }
}