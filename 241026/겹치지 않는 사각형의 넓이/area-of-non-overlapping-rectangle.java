import java.util.Scanner;

public class Main {
    public static final int MAX_N = 2000;
    public static int[][] grid = new int[MAX_N + 1][MAX_N + 1];
    public static final int OFFSET = 1000;
    
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
    
        int ax1 = sc.nextInt();
        int ay1 = sc.nextInt();
        int ax2 = sc.nextInt();
        int ay2 = sc.nextInt();

        for (int i = ax1 + OFFSET; i < ax2 + OFFSET; i++) {
            for (int j = ay1 + OFFSET; j < ay2 + OFFSET; j++) {
                grid[i][j] = 1;
            }
        }

        int bx1 = sc.nextInt();
        int by1 = sc.nextInt();
        int bx2 = sc.nextInt();
        int by2 = sc.nextInt();

        for (int i = bx1 + OFFSET; i < bx2 + OFFSET; i++) {
            for (int j = by1 + OFFSET; j < by2 + OFFSET; j++) {
                grid[i][j] = 1;
            }
        }

        int mx1 = sc.nextInt();
        int my1 = sc.nextInt();
        int mx2 = sc.nextInt();
        int my2 = sc.nextInt();

        for (int i = mx1 + OFFSET; i < mx2 + OFFSET; i++) {
            for (int j = my1 + OFFSET; j < my2 + OFFSET; j++) {
                grid[i][j] = 0;
            }
        }

        int cnt = 0;
        for (int i = 0; i < MAX_N; i++) {
            for (int j = 0; j < MAX_N; j++) {
                if (grid[i][j] > 0) {
                    cnt += 1;
                }
            }
        }

        System.out.println(cnt);
    }
}