import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();

        int[] wArray = new int[n + 1];
        int[] oArray = new int[n + 1];
        int[] owArray = new int[n + 1];

        for (int i = n - 1; i >= 0; i--) {
            if (str.charAt(i) == 'W') {
                wArray[i] = wArray[i + 1] + 1;
                oArray[i] = oArray[i + 1];
                owArray[i] = owArray[i + 1];
            } else if (str.charAt(i) == 'O') {
                wArray[i] = wArray[i + 1];
                oArray[i] = oArray[i + 1] + 1;
                owArray[i] = owArray[i + 1] + wArray[i];
            } else {
                owArray[i] = owArray[i + 1];
                wArray[i] = wArray[i + 1];
                oArray[i] = oArray[i + 1];
            }
        }

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (str.charAt(i) == 'C') {
                cnt += owArray[i];
            }
        }

        System.out.println(cnt);
    }
}