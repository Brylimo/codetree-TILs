import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] stairs = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            stairs[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[n + 1][4];
        
        // 초기화
        for (int i = 0; i < n + 1; i++) {
            Arrays.fill(dp[i], INT_MIN);
        }
        dp[0][1] = dp[0][2] = dp[0][3] = 0;

        dp[1][1] = stairs[0];
        dp[2][0] = stairs[1];
        dp[2][2] = dp[1][1] + stairs[1];

        for (int i = 3; i < n + 1; i++) {
            if (dp[i-2][0] != INT_MIN)
                dp[i][0] = dp[i - 2][0] + stairs[i - 1];
            if (dp[i - 1][0] != INT_MIN && dp[i - 2][1]!= INT_MIN)
                dp[i][1] = Math.max(dp[i - 1][0], dp[i - 2][1]) + stairs[i - 1];
            if (dp[i - 1][1] != INT_MIN && dp[i - 2][2] != INT_MIN)
                dp[i][2] = Math.max(dp[i - 1][1], dp[i - 2][2]) + stairs[i - 1];
            if (dp[i - 1][2] != INT_MIN && dp[i - 2][3]!= INT_MIN)
                dp[i][3] = Math.max(dp[i - 1][2], dp[i - 2][3]) + stairs[i - 1];
        }

        int ans = INT_MIN;
        dp[n][1] = 0;
        for (int i : dp[n]) {
            ans = Math.max(ans, i);
        }

        System.out.println(ans);
    }
}