import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
    
        int cnt = 0;
        int maxVal = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (i == 0 || arr[i] * arr[i - 1] > 0) {
                cnt += 1;
            } else {
                cnt = 1;
            }

            maxVal = Math.max(maxVal, cnt);
        }

        System.out.println(maxVal);
    }
}