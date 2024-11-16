import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int maxVal = INT_MIN;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (sum < 0) {
                sum = arr[i];
            } else {
                sum += arr[i];
            }

            maxVal = Math.max(maxVal, sum);
        }

        System.out.println(maxVal);
    }
}