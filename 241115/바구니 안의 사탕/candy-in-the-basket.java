import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;
    public static final int MAX_N = 1000000;
    public static int[] line = new int[MAX_N + 1];

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 사탕을 집어넣음
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int candy = Integer.parseInt(st.nextToken());
            int idx = Integer.parseInt(st.nextToken());

            line[idx] = candy; 
        }

        int sumVal = 0;
        for (int i = 0; i <= k + 1; i++) {
            if (i <= MAX_N)
                sumVal += line[i];
        }
        int cnt = k + 1;

        int maxVal = sumVal;
        int current = cnt;

        while (current - k <= MAX_N) {
            if (cnt >= 2 * k + 1) {
                sumVal -= line[current - (2 * k)];
                cnt -= 1;
            }
            current += 1;

            if (current > MAX_N) break;

            if (current <= MAX_N)
                sumVal += line[current];
                cnt += 1;

            maxVal = Math.max(maxVal, sumVal);
        }

        System.out.println(maxVal);
    }
}