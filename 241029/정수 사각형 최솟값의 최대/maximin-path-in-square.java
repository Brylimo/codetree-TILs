import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][][] dp = new int[n][n][2];

        // 초기화
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 2; k++) {
                    dp[i][j][k] = INT_MAX;
                }
            }
        }

        dp[0][0][0] = dp[0][0][1] = arr[0][0];

        // 가로 초기화
        for (int i = 1; i < n; i++) {
            dp[0][i][0] = Math.min(Math.min(dp[0][i - 1][0], dp[0][i - 1][1]), arr[0][i]);
                        dp[0][i][1] = Math.min(Math.min(dp[0][i - 1][0], dp[0][i - 1][1]), arr[0][i]);
        }

        // 세로 초기화
        for (int i = 1; i < n; i++) {
            dp[i][0][1] = Math.min(Math.min(dp[i - 1][0][0], dp[i - 1][0][1]), arr[i][0]);
            dp[i][0][0] = Math.min(Math.min(dp[i - 1][0][0], dp[i - 1][0][1]), arr[i][0]);
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j][0] = Math.min(Math.max(dp[i][j - 1][1], dp[i][j - 1][0]), arr[i][j]);
                dp[i][j][1] = Math.min(Math.max(dp[i - 1][j][0], dp[i - 1][j][1]), arr[i][j]);
            }
        }

        System.out.println(Math.max(dp[n - 1][n - 1][0], dp[n - 1][n - 1][1]));

    }
}