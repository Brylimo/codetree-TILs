import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 1000000;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] arr = new int[MAX_N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());

            arr[x] = 1;
        }

        int[] prefixSum = new int[MAX_N + 1];
        prefixSum[0] = arr[0];
        for (int i = 1; i < MAX_N + 1; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        } 

        while (q-- > 0) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            sb.append(prefixSum[b] - prefixSum[a] + arr[a]).append('\n');
        }

        System.out.print(sb);
    }
}