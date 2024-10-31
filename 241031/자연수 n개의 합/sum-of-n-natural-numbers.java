import java.util.*;
import java.io.*;

public class Main {
    public static long s;

    public static long binarySearch() {
        long left = 1;
        long right = Integer.MAX_VALUE;

        long ans = 0;
        while (left <= right) {
            long mid = (left + right) / 2;

            if (mid * (mid + 1) / 2 <= s) {
                left = mid + 1;

                ans = Math.max(ans, mid);
            } else {
                right = mid - 1;
            }
        }

        return ans;
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = Long.parseLong(br.readLine());

        long ans = binarySearch();

        System.out.println(ans);
    }
}