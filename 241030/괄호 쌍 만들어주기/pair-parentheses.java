import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] array = br.readLine().toCharArray();

        int len = array.length;
        int[] R = new int[len];
        
        for (int i = len - 2; i >= 0; i--) {
            if (array[i] == ')' && array[i + 1] == ')')
                R[i] = R[i + 1] + 1;
            else
                R[i] = R[i + 1];
        }

        //System.out.println(Arrays.toString(R));

        int cnt = 0;
        for (int i = 0; i < len - 1; i++) {
            if (array[i] == '(' && array[i + 1] == '(') {
                cnt += R[i + 1];
            }
        }

        System.out.println(cnt);
    }
}