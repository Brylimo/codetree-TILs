import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        Queue<Integer> queue = new LinkedList<>();
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());

            String option = st.nextToken();
            if (option.equals("push")) {
                int a = Integer.parseInt(st.nextToken());
                queue.add(a);
            } else if (option.equals("pop")) {
                if (!queue.isEmpty()) {
                    int res = queue.poll();
                    System.out.println(res);
                }
            } else if (option.equals("size")) {
                System.out.println(queue.size());
            } else if (option.equals("empty")) {
                if (queue.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if (option.equals("front")) {
                System.out.println(queue.peek());
            }
        }
    }
}