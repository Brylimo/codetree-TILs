import java.util.Scanner;

public class Main {
    public static final int OFFSET = 100;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int[][] grid = new int[200][200];

        int n = sc.nextInt();
        for (int k = 0; k < n; k++) {
            int x1, y1, x2, y2;
            x1 = sc.nextInt();
            y1 = sc.nextInt();
            x2 = sc.nextInt();
            y2 = sc.nextInt();

            for (int i = x1; i < x2; i++) {
                for (int j = y1; j < y2; j++) {
                    grid[i][j] = 1;
                }
            }
        }

        int cnt = 0;
        for (int i = 0; i < 200; i++) {
            for (int j = 0; j < 200; j++) {
                if (grid[i][j] > 0) {
                    cnt += 1;
                }
            }
        }

        System.out.println(cnt);
    }
}