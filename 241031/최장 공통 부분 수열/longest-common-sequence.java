import java.util.*;

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();

        int lenA = a.length();
        int lenB = b.length();
        int[][] dp = new int[lenA][lenB];

        /*for (int i = 0; i < lenA; i++) {
            Arrays.fill(dp[i], INT_MIN);
        }*/

        if (a.charAt(0) == b.charAt(0))
            dp[0][0] = 1;

        for (int i = 1; i < lenA; i++) {
            if (a.charAt(i) == b.charAt(0))
                dp[i][0] = 1;
            else
                dp[i][0] = dp[i - 1][0];
        }

        for (int i = 1; i < lenB; i++) {
            if (a.charAt(0) == b.charAt(i))
                dp[0][i] = 1;
            else
                dp[0][i] = dp[0][i - 1];
        }

        for (int i = 1; i < lenA; i++) {
            for (int j = 1; j < lenB; j++) {
                if (a.charAt(i) == b.charAt(j)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }

        System.out.println(dp[lenA - 1][lenB - 1]);
    }
}