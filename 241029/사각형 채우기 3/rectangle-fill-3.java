import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 1000, MOD_N = 1000000007;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[MAX_N + 1];

        dp[0] = 1;
        dp[1] = 2;
        dp[2] = 7;
        for (int i = 3; i <= n; i++) {
            int sum = 0;
            for (int j = 0; j <= i - 3; j++) {
                sum += dp[j] % MOD_N;
            }
            dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3 + 2*sum) % MOD_N;
        }

        System.out.println(dp[n]);
    }
}