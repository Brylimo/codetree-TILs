import java.util.*;
import java.io.*;

class Suite {
    int s, e, v;

    public Suite(int s, int e, int v) {
        this.s = s;
        this.e = e;
        this.v = v;
    }
}

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<Suite> suites = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            suites.add(new Suite(s, e, v));
        }

        int[][] dp = new int[m + 1][n];
        for (int i = 0; i <= m; i++) {
            Arrays.fill(dp[i], INT_MIN);
        }

        // initialize
        for (int i = 0; i < n; i++) {
            if (suites.get(i).s == 1)
                dp[1][i] = 0;
        }

        for (int i = 2; i <= m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (dp[i - 1][k] == INT_MIN) continue;

                    if (suites.get(j).s <= i && suites.get(j).e >= i)
                        dp[i][j] = Math.max(dp[i][j], dp[i - 1][k] + Math.abs(suites.get(k).v - suites.get(j).v));
                }
            }
        }

        /*for (int i = 1; i <= m; i++) {
            System.out.println(Arrays.toString(dp[i]));
        }*/

        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, dp[m][i]);
        }

        System.out.println(ans);
    }
}