import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int ans = Integer.MAX_VALUE;
        boolean flag = false;

        int cnt = 0;
        while (n > 0) {
            if (n % 2 == 0) {
                ans = Math.min(ans, cnt + n / 2);
                flag = true;
            }

            //System.out.println(ans);
            cnt += 1;
            n -= 5;
        }

        if (n == 0 && !flag) {
            flag = true;
            ans = Math.min(ans, cnt);
        }

        if (!flag) {
            System.out.println(-1);            
        } else {
            System.out.println(ans);
        }
    }
}