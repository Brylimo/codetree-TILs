import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] coins = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[m + 1];
        Arrays.fill(dp, INT_MAX);

        dp[0] = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 0; j < n; j++) {
                if (i >= coins[j]) {

                    if (dp[i-coins[j]] == INT_MAX) continue;

                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }

        if (dp[m] == INT_MAX) System.out.println(-1);
        else {
            System.out.println(dp[m]);
        }
    }
}