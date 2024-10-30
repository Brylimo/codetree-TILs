import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // two pointer
        int ans = 100100;
        int sum = 0;

        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j + 1 < n && sum + arr[j + 1] < s) {
                sum += arr[j + 1];

                j += 1;
            }

            ans = Math.min(ans, j + 1 - i + 1);
            sum -= arr[i];
        }

        if (ans == 100100) {
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }
    }
}