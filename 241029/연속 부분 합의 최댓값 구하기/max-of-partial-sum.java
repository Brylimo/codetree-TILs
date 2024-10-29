import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n + 1];
        Arrays.fill(dp, INT_MIN);

        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i] = Math.max(dp[i - 1] + arr[i - 1], arr[i - 1]);
        }

        int ans = INT_MIN;
        for (int i = 1; i <= n; i++) {
            ans = Math.max(ans, dp[i]);
        }

        System.out.println(ans);
    }
}