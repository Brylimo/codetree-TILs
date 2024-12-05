import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        boolean[][] graph = new boolean[n + 1][n + 1];

        for (int i = 0; i <= n; i++) {
            graph[i][i] = true;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a][b] = true;
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (graph[i][k] && graph[k][j]) {
                        graph[i][j] = true;
                    }
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            int cnt = 0;
            for (int j = 1; j <= n; j++) {
                if (!graph[i][j] && !graph[j][i]) {
                    cnt += 1;
                }
            }

            System.out.println(cnt);
        }
    }
}