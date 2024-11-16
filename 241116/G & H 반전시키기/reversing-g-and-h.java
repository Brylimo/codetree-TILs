import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String initial = br.readLine();
        String target = br.readLine();

        int[] array = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            if (initial.charAt(i - 1) != target.charAt(i - 1)) {
                array[i] = 1;
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (array[i] == 0 && array[i + 1] == 1) {
                ans += 1;
            }
        }

        System.out.println(ans);
    }
}