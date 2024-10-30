import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        ArrayList<Integer>[] R = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            R[i] = new ArrayList<>();
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = 1; j <= k; j++) {
                if (i + j < n) {
                    R[i].add(arr[i + j]);
                }
                if (i - j >= 0) {
                    R[i].add(arr[i - j]);
                }
            }
        }

        int maxNum = -1;
        for (int i = 0; i < n; i++) {
            if (R[i].indexOf(arr[i]) != -1)
                maxNum = Math.max(maxNum, arr[i]);
        }

        System.out.println(maxNum);
    }
}