import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 100;
    public static int[][] graph = new int[MAX_N][MAX_N];
    public static int[][] dp = new int[MAX_N][MAX_N];

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
    
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = graph[0][0];
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i - 1] + graph[0][i];
            dp[i][0] = dp[i - 1][0] + graph[i][0];
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]) + graph[i][j];
            }
        }

        System.out.println(dp[n - 1][n - 1]);
    }
}