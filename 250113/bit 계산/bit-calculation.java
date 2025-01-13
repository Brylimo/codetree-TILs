import java.util.*;
import java.io.*;

public class Main {
    static int snum;

    public static void main(String[] args) throws IOException {
        // Please write your code here.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int q = Integer.parseInt(br.readLine());
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());

            String op = st.nextToken();

            if (op.equals("add")) {
                int x = Integer.parseInt(st.nextToken());

                if (((snum >> x) & 1) != 1) {
                    snum ^= (1 << x);
                }
            } else if (op.equals("delete")) {
                int x = Integer.parseInt(st.nextToken());

                if (((snum >> x) & 1) == 1) {
                    snum ^= (1 << x);
                }
            } else if (op.equals("print")) {
                int x = Integer.parseInt(st.nextToken());

                if (((snum >> x) & 1) == 1) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if (op.equals("toggle")) {
                int x = Integer.parseInt(st.nextToken());

                snum = snum ^ (1 << x);
            } else if (op.equals("clear")) {
                snum = 0;
            }
        }
    }
}