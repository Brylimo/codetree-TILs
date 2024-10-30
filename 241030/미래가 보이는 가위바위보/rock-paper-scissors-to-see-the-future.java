import java.util.*;
import java.io.*;

public class Main {
    static final int INT_MIN = Integer.MIN_VALUE;

    public static int win(char a, char b) {
        if (a == 'P' && b == 'S') {
            return 1;
        }
        if (a == 'S' && b == 'H') {
            return 1;
        }
        if (a == 'H' && b == 'P') {
            return 1;
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        
        char[] pos = new char[n];
        for (int i = 0; i < n; i++) {
            pos[i] = br.readLine().charAt(0);
        }

        int[][] L = new int[3][n];
        for (int i = 0; i < 3; i++) { // 0 -> h, 1 -> s, 2 -> p
            char temp = 'H';

            if (i == 0) temp = 'H';
            else if (i == 1) temp = 'S';
            else if (i == 2) temp = 'P';
            
            L[i][0] = win(pos[0], temp);
            for (int j = 1; j < n; j++) {
                L[i][j] = L[i][j - 1] + win(pos[j], temp); 
            }
        }

        int[][] R = new int[3][n];
        for (int i = 0; i < 3; i++) { // 0 -> h, 1 -> s, 2 -> p
            char temp = 'H';

            if (i == 0) temp = 'H';
            else if (i == 1) temp = 'S';
            else if (i == 2) temp = 'P';
            
            R[i][n-1] = win(pos[n - 1], temp);
            for (int j = n - 2; j >= 0; j--) {
                R[i][j] = R[i][j + 1] + win(pos[j], temp); 
            }
        }

        int ans = Math.max(Math.max(L[0][n - 1], L[1][n - 1]), L[2][n - 1]);
        for (int i = 0; i < 3; i++) {
            for (int j = 1; j < n; j++) {
                for (int k = 0; k < 3; k++) {
                    if (i == k) continue;

                    ans = Math.max(ans, L[i][j - 1] + R[k][j]);
                }
            }
        }

        /*for (int i = 0; i < 3; i++) {
            System.out.println(Arrays.toString(R[i]));
        }*/

        System.out.println(ans);
    }
}