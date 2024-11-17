import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] arr = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int[][] prefixSum = new int[n + 1][4];

        for (int i = 1; i <= n; i++) {
            int group = arr[i];

            for (int j = 1; j <= 3; j++) {
                prefixSum[i][j] = prefixSum[i - 1][j];
            }

            prefixSum[i][group] += 1;
        }

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());


            int first = prefixSum[b][1] - prefixSum[a - 1][1];
            int second = prefixSum[b][2] - prefixSum[a - 1][2];
            int third = prefixSum[b][3] - prefixSum[a - 1][3];
        
            System.out.println(first + " " + second + " " + third);
        }

    }
}