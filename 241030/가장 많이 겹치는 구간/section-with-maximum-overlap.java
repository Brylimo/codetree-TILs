import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 100001;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        int[] line = new int[MAX_N];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
        
            line[x1] = 1;
            line[x2] = -1;
        }

        int ans = 0;
        int sum = 0;
        for (int i = 0; i < MAX_N; i++) {
            sum += line[i];
            ans = Math.max(ans, sum);
        }

        System.out.println(ans);
    }
}