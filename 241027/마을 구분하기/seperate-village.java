import java.util.*;

public class Main {
    public static final int MAX_N = 25;

    public static int n, cnt;
    public static int[][] graph = new int[MAX_N][MAX_N];
    public static boolean[][] visited = new boolean[MAX_N][MAX_N];

    public static int[] dx = new int[]{-1, 0, 1, 0};
    public static int[] dy = new int[]{0, 1, 0, -1};

    public static boolean inRange(int x, int y) {
        return (0 <= x && x < n && 0 <= y && y < n);
    }

    public static void dfs(int num, int x, int y) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!inRange(nx, ny)) continue;

            if (!visited[nx][ny] && graph[nx][ny] == 1) {
                visited[nx][ny] = true;
                cnt += 1;
                dfs(num, nx, ny);
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

        ArrayList<Integer> array = new ArrayList<>();

        int total = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && graph[i][j] == 1) {
                    visited[i][j] = true;
                    total += 1;
                    cnt = 1;
                    dfs(total, i, j);
                    array.add(cnt);
                }
            }
        }

        Collections.sort(array);

        System.out.println(total);
        for (int i = 0; i < total; i++) {
            System.out.println(array.get(i));
        }
    }
}