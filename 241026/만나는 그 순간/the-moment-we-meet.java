import java.util.*;

public class Main {
    public static int[] grid1 = new int[1000000];
    public static int[] grid2 = new int[1000000];

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int idx = 1;
        for (int i = 0; i < n; i++) {
            int d = sc.next().charAt(0);
            int t = sc.nextInt();

            for (int j = idx; j < idx + t; j++) {
                if (d == 'R') {
                    grid1[j] = grid1[j - 1] + 1;
                } else if (d == 'L') {
                    grid1[j] = grid1[j - 1] - 1;
                }
            }
            idx += t;
        }

        int cntA = idx;

        idx = 1;
        for (int i = 0; i < m; i++) {
            int d = sc.next().charAt(0);
            int t = sc.nextInt();

            for (int j = idx; j < idx + t; j++) {
                if (d == 'R') {
                    grid2[j] = grid2[j - 1] + 1;
                } else if (d == 'L') {
                    grid2[j] = grid2[j - 1] - 1;
                }
            }
            idx += t;
        }

        int cntB = idx;

        int max = Math.max(cntA, cntB);
        for (int i = 1; i < 1000000; i++) {
            if (i == max) {
                System.out.println(-1);
                break;
            }

            if (grid1[i] == grid2[i]) {
                System.out.println(i);
                break;
            }
        }
    }
}