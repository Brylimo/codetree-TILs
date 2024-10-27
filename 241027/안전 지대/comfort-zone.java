import java.util.*;

public class Main {
    public static final int MAX_N = 50;
    public static final int MAX_K = 100;

    public static int n, m;
    public static int[] dx = new int[]{-1, 0, 1, 0};
    public static int[] dy = new int[]{0, 1, 0, -1};
    
    public static int[][] graph = new int[MAX_N][MAX_N];
    public static boolean[][] visited = new boolean[MAX_N][MAX_N];
    public static ArrayList<Temp> safes = new ArrayList<>();

    public static boolean inRange(int x, int y) {
        return (0 <= x && x < n && 0 <= y && y < m);
    }

    public static void dfs(int k, int x, int y) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!inRange(nx, ny)) continue;

            if (!visited[nx][ny] && graph[nx][ny] > k) {
                visited[nx][ny] = true;

                dfs(k, nx, ny);
            }
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

        // k의 개수 정함
        for (int k = 1; k < MAX_K + 1; k++) {
            // dfs
            int cntNum = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (!visited[i][j] && graph[i][j] > k) {
                        visited[i][j] = true;
                        cntNum += 1;
                        dfs(k, i, j);
                    }
                }
            }

            safes.add(new Temp(k, cntNum));
            // 초기화
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    visited[i][j] = false;
                }
            }
        }

        Collections.sort(safes);

        System.out.println(safes.get(0).k + " " + safes.get(0).cnt);
    }

    static class Temp implements Comparable<Temp> {
        int k;
        int cnt;

        public Temp(int k, int cnt) {
            this.k = k;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Temp temp) {
            return temp.cnt - this.cnt;
        }
    }
}