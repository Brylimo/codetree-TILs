import java.util.*;
import java.io.*;

public class Main {
    public static int n, m;
    public static int[] arr;

    public static boolean isPossible(int mid) {       
        if (mid == 0) return false;

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            cnt += arr[i] / mid;
        }

        return (cnt >= m);
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int left = 0;
        int right = 100000;

        int ans = 0;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (isPossible(mid)) {
                left = mid + 1;

                ans = Math.max(ans, mid);
            } else {
                right = mid - 1;
            }
        }

        System.out.println(ans);
    }
}