import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;
    public static int n;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] prefixSum = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + arr[i][j];
            }
        }

        int maxVal = INT_MIN;

        // (i, j) ~ (i - k, j - k)
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i >= k && j >= k) {
                    int res = prefixSum[i][j] - prefixSum[i - k][j] - prefixSum[i][j - k] + prefixSum[i - k][j - k];
               
                    maxVal = Math.max(maxVal, res);
                }
            }
        }

        System.out.println(maxVal);
    }
}