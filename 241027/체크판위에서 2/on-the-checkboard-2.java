import java.util.Scanner;

public class Main {
    public static char[][] grid;
    public static int r, c, ans;

    public static boolean inRange(int x, int y) {
        return (0 <= x && x < r && 0 <= y && y < c);
    }

    public static void jump(char current, int x, int y, int score) {
        if (x == r - 1 && y == c - 1) {
            if (score - 1 == 2) ans += 1;
            return;
        }

        for (int a = x + 1; a < r; a++) {
            for (int b = y + 1; b < c; b++) {
                char target = grid[a][b];

                if (current != target) {
                    jump(target, a, b, score + 1);
                }
            }
        }

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

        char current = grid[0][0];
        jump(current, 0, 0, 0);
    
        System.out.println(ans);
    }
}