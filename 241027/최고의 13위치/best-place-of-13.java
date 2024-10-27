import java.util.Scanner;

public class Main {
    public static final int INT_MAX = Integer.MIN_VALUE;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }

        int maxVal = INT_MAX;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 2; j++) {
                maxVal = Math.max(maxVal, grid[i][j] + grid[i][j + 1] + grid[i][j + 2]);
            }
        }
    
        System.out.println(maxVal);
    }
}