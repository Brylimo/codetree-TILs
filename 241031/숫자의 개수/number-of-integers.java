import java.util.*;
import java.io.*;

public class Main {
    public static int n, m;
    public static int[] arr;

    public static int lowerBound(int x) {
        int left = 0;
        int right = n - 1;

        int idx = n;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] >= x) {
                right = mid - 1;
                idx = Math.min(idx, mid);
            } else {
                left = mid + 1;
            }
        }

        return idx;
    }

    public static int upperBound(int x) {
        int left = 0;
        int right = n - 1;

        int idx = n;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] > x) {
                right = mid - 1;
                idx = Math.min(idx, mid);
            } else {
                left = mid + 1;
            }
        }

        return idx;
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

        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(br.readLine());

            int a = lowerBound(x);
            int b = upperBound(x);

            System.out.println(b - a);
        }
    }
}