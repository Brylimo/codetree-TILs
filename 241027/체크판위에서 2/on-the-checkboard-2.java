import java.util.Scanner;

public class Main {
    public static char[][] grid;
    public static int r, c;

    public static int jump(char current, int x, int y, int score) {
        if (x == r - 1 || y == c - 1) return score;

        for (int a = x + 1; a < r; a++) {
            for (int b = y + 1; b < c; b++) {
                char target = grid[a][b];

                if (current != target) {
                    return jump(target, a, b, score + 1);
                }
            }
        }

        return score;
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        r = sc.nextInt();
        c = sc.nextInt();

        grid = new char[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                grid[i][j]= sc.next().charAt(0);
            }
        }

        int ans = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                char current = grid[i][j];

                int count = jump(current, i, j, 0);

                if (count == 3) ans += 1;
            }
        }
    
        System.out.println(ans);
    }
}