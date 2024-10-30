import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 100000;

    public static int n;
    public static int[] arr = new int[MAX_N + 1];

    public static int bisect(int x) {

        int left = 0;
        int right = n - 1;

        int index = -1;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] == x) {
                index = mid + 1;
                break;
            }

            if (arr[mid] < x) {
                left = mid + 1;
            } else if (arr[mid] > x) {
                right = mid - 1;
            }
        }

        return index;
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(br.readLine());

            int idx = bisect(x);
            System.out.println(idx);
        }
    }
}