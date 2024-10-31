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

    public static int customBound(int x) {
        int left = 0;
        int right = n - 1;
        int idx = -1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] <= x) {
                left = mid + 1;

                idx = Math.max(idx, mid);
            } else {
                right = mid - 1;
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

        st = new StringTokenizer(br.readLine());
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int leftIdx = lowerBound(a);
            int rightIdx = customBound(b);

            if (leftIdx > rightIdx) System.out.println(0);
            else System.out.println(rightIdx - leftIdx + 1);
        
        }
    }
}