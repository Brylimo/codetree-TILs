import java.util.*;

public class Main {
    public static final int MAX_N = (int)Math.pow(10, 9);
    public static int n;

    public static int binarySearch() {
        int start = 1;
        int end = MAX_N;

        while (start <= end) {
            int mid = (start + end) / 2;

            int res1 = mid / 3;
            int res2 = mid / 5;

            int res = res1 + res2;

            if (mid % 3 == 0) res -= 1;
            if (mid % 5 == 0) res -= 1;

            if (mid - res == n) {
                return mid;
            }

            if (mid - res > n) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return -1;
    }
    
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        int ans = binarySearch();

        System.out.println(ans);
    }
}