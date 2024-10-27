import java.util.*;

public class Main {
    public static int n, m, x, y, dir, cnt;
    public static int[][] grid;
    public static int[] dx = new int[]{-1, 0, 1, 0};
    public static int[] dy = new int[]{0, 1, 0, -1};

    public static boolean inRange(int x, int y) {
        return (0 <= x && x < n && 0 <= y && y < m);
    }

    public static void simulate() {
        
        while (true) {
            if (cnt > n*m) break;

            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (inRange(nx, ny) && grid[nx][ny] == 0) {
                grid[nx][ny] = cnt++;
                x = nx; y = ny;
            } else {
                dir = (dir + 1) % 4;
            }   
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        cnt = 1;
        dir = 1;
        grid = new int[n][m];
        grid[0][0] = cnt++;

        x = 0; y = 0;
        simulate();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }
}