import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 1000;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[MAX_N + 1];

        dp[2] = 1;
        dp[3] = 1;
        for (int i = 4; i <= n; i++) {
            dp[i] = (dp[i - 2] + dp[i - 3]) % 10007;
        }

        System.out.println(dp[n]);
    }
}