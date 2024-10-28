import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            String option = st.nextToken();

            if (option.equals("push")) {
                int a = Integer.parseInt(st.nextToken());

                pq.add(-a);
            } else if (option.equals("pop")) {
                if (!pq.isEmpty()) {
                    int x = pq.poll();
                    System.out.println(-x);
                }
            } else if (option.equals("size")) {
                System.out.println(pq.size());
            } else if (option.equals("empty")) {
                if (pq.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if (option.equals("top")) {
                System.out.println(-pq.peek());
            }
        }

    }
}