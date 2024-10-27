import java.util.*;

public class Main {
    public static final int MAX_N = 100;

    public static int blockCnt, n;
    public static int[][] graph = new int[MAX_N][MAX_N];
    public static boolean[][] visited = new boolean[MAX_N][MAX_N];
    public static ArrayList<Integer> blocks = new ArrayList<>();

    public static boolean inRange(int x, int y) {
        return (0 <= x && x < n && 0 <= y && y < n);
    }

    public static void dfs(int x, int y) {
        int[] dx = new int[]{-1, 0, 1, 0};
        int[] dy = new int[]{0, 1, 0, -1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!inRange(nx, ny)) continue;

            if (!visited[nx][ny] && graph[nx][ny] == graph[x][y]) {
                visited[nx][ny] = true;

                blockCnt += 1;
                dfs(nx, ny);
            }
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        int bombCnt = 0;
        int maxBlockSize = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    visited[i][j] = true;
                    blockCnt = 1;
                    dfs(i, j);

                    if (blockCnt >= 4) {
                        bombCnt += 1;
                    }

                    if (maxBlockSize < blockCnt) {
                        maxBlockSize = blockCnt;
                    }

                }
            }
        }

        System.out.println(bombCnt + " " + maxBlockSize);
    }
}