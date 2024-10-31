import java.util.*;
import java.io.*;

public class Main {
    public static int n, m;
    public static int[] arr;

    public static int lowerBound(int x) {
        int left = 0;
        int right = n - 1;

        int idx = n;
        int target = x;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] >= target) {
                right = mid - 1;

                idx = Math.min(idx, mid);
            } else {
                left = mid + 1;
            }
        }

        return idx + 1;
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(st.nextToken());

            int ans = lowerBound(x);

            if ((ans - 1 < n && arr[ans - 1] != x)) System.out.println(-1);
            else System.out.println(ans);
        }
    }
}