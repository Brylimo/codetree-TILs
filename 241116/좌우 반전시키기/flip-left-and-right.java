import java.util.*;
import java.io.*;

public class Main {
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

        int ans = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i - 1] == 0) {
                ans += 1;

                if (arr[i - 1] == 1) {
                    arr[i - 1] = 0;
                } else {
                    arr[i - 1] = 1;
                }

                if (arr[i] == 1) {
                    arr[i] = 0;
                } else {
                    arr[i] = 1;
                }

                if (i + 1 < n) {
                    if (arr[i + 1] == 1) {
                        arr[i + 1] = 0;
                    } else {
                        arr[i + 1] = 1;
                    }
                }
            }
        }

        if (arr[n - 1] == 0) {
            System.out.println(-1);
        } else {
            System.out.println(ans);
        }

    }
}