import java.util.*;

public class Main {
    public static final int MAX_N = 100;
    public static int n, m, ans;
    public static int[] dx = new int[]{0, 1};
    public static int[] dy = new int[]{1, 0};

    public static int[][] graph = new int[MAX_N][MAX_N];
    public static boolean[][] visited = new boolean[MAX_N][MAX_N];

    public static boolean inRange(int x, int y) {
        return (0 <= x && x < n && 0 <= y && y < m);
    }

    public static void dfs(int x, int y) {
        if (x == n - 1 && y == m - 1) {
            ans = 1;
            return;
        }

        for (int i = 0; i < 2; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!inRange(nx, ny)) {
                continue;
            }

            if (!visited[nx][ny] && graph[nx][ny] == 1) {
                visited[nx][ny] = true;
                dfs(nx, ny);
            }
        }
    }

    public static void print() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(visited[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        visited[0][0] = true;
        dfs(0, 0);

        //print();

        System.out.println(ans);
    }
}