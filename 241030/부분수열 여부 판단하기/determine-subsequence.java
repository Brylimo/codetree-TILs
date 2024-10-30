import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] a = new int[n + 1];
        int[] b = new int[m + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= m; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        boolean flag = true;
        int j = 1;
        for (int i = 1; i <= m; i++) {
            while (j <= n && a[j] != b[i]) {
                j += 1;
            }

            if (j == n + 1) {
                flag = false;
                break;
            }
        }

        if (flag) System.out.println("Yes");
        else System.out.println("No");
    }
}