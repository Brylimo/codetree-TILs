import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        char[][] arr = new char[n][m];

        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine().toCharArray();
        }

        int[][] prefixSumA = new int[n + 1][m + 1];
        int[][] prefixSumB = new int[n + 1][m + 1];
        int[][] prefixSumC = new int[n + 1][m + 1];

        // 누적합 초기화
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (arr[i - 1][j - 1] == 'a')
                    prefixSumA[i][j] = prefixSumA[i - 1][j] + prefixSumA[i][j - 1] - prefixSumA[i - 1][j - 1] + 1;
                else
                    prefixSumA[i][j] = prefixSumA[i - 1][j] + prefixSumA[i][j - 1] - prefixSumA[i - 1][j - 1];
                if (arr[i - 1][j - 1] == 'b')
                    prefixSumB[i][j] = prefixSumB[i - 1][j] + prefixSumB[i][j - 1] - prefixSumB[i - 1][j - 1] + 1;
                else
                    prefixSumB[i][j] = prefixSumB[i - 1][j] + prefixSumB[i][j - 1] - prefixSumB[i - 1][j - 1];
                if (arr[i - 1][j - 1] == 'c')
                    prefixSumC[i][j] = prefixSumC[i - 1][j] + prefixSumC[i][j - 1] - prefixSumC[i - 1][j - 1] + 1;
                else
                    prefixSumC[i][j] = prefixSumC[i - 1][j] + prefixSumC[i][j - 1] - prefixSumC[i - 1][j - 1];
            }
        }

        /*for (int i = 1; i <= n; i++) {
            System.out.println(Arrays.toString(prefixSumA[i]));
        }*/

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int r1 = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());

            int sumA = prefixSumA[r2][c2] - prefixSumA[r2][c1 - 1] - prefixSumA[r1 - 1][c2] + prefixSumA[r1 - 1][c1 - 1];
            int sumB = prefixSumB[r2][c2] - prefixSumB[r2][c1 - 1] - prefixSumB[r1 - 1][c2] + prefixSumB[r1 - 1][c1 - 1];
            int sumC = prefixSumC[r2][c2] - prefixSumC[r2][c1 - 1] - prefixSumC[r1 - 1][c2] + prefixSumC[r1 - 1][c1 - 1];
        
            System.out.println(sumA + " " + sumB + " " + sumC);
        }
        

    }
}