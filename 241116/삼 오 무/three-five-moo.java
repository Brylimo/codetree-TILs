import java.util.*;

public class Main {
    public static final int MAX_N = Integer.MAX_VALUE;
    public static int n;

    public static long binarySearch() {
        long start = 1;
        long end = MAX_N;

        while (start <= end) {
            long mid = (start + end) / 2;

            long res1 = mid / 3;
            long res2 = mid / 5;
            long res3 = mid / 15;

            long res = res1 + res2 - res3;

            if (mid - res == n) {
                if (mid % 3 == 0 || mid % 5 == 0) {
                    end = mid - 1;
                    continue;
                }
                
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

        long ans = binarySearch();

        System.out.println(ans);
    }
}