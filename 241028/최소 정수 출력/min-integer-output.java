import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            int x = Integer.parseInt(br.readLine());

            if (x > 0) {
                pq.add(x);
            } else if (x == 0) {
                if (!pq.isEmpty()) {
                    int res = pq.poll();
                    System.out.println(res);
                } else {
                    System.out.println(0);
                }
            }
        }
    }
}