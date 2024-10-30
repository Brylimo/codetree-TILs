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

        int[] arr = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int ans = 0;
        int sum = 0;
        int j = 0;
        for (int i = 1; i <= n; i++) {
            while (j + 1 <= n && sum + arr[j + 1] <= m) {
                sum += arr[j + 1];
                j += 1;
            }

            if (sum == m) {
                ans += 1;
            }

            sum -= arr[i];
        }

        System.out.println(ans);
    }
}