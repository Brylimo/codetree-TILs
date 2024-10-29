import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int[] arr = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            arr[i] = 1;
        }

        for (int i = 0; i < b; i++) {
            int x = Integer.parseInt(br.readLine());

            arr[x] = 0;
        }

        int[] prefixSum = new int[n + 1];
        prefixSum[1] = arr[1];
        for (int i = 2; i <= n; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }

        int minVal = INT_MAX;
        // 전체 순환 -> 최소개수 구함
        for (int i = 1; i <= n - k; i++) {
            minVal = Math.min(minVal, k - (prefixSum[i + k] - prefixSum[i]));
        }

        System.out.println(minVal);
    }
}