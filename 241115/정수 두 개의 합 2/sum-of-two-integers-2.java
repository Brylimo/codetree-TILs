import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int ans = 0;
        int i = 0;
        int j = n - 1;
        while (i < j) {
            while (j > 0 && arr[i] + arr[j] > k) {
                j -= 1;
            }

            i += 1;
            ans += j - i + 1;
        }

        System.out.println(ans);
    }
}