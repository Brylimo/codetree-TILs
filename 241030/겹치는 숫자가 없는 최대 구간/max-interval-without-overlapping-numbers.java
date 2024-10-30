import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_NUM = 100000;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int[] arr = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] countArray = new int[MAX_NUM + 1];

        int ans = 0;
        int j = 0;
        for (int i = 1; i <= n; i++) {

            while (j + 1 <= n && countArray[arr[j + 1]] != 1) {
                countArray[arr[j + 1]] += 1;
                j += 1;
            }

            ans = Math.max(ans, j - i + 1);
            countArray[arr[i]] -= 1;
        }

        System.out.println(ans);
    }
}