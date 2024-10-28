import java.util.*;
import java.io.*;

public class Main {
    public static Queue<Integer> q = new LinkedList<>();
    
    public static void print() {
        for (int i = 0; i < q.size(); i++) {
            System.out.print(((LinkedList)q).get(i));
        }
        System.out.println();
    }

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            q.add(i);
        }

        int cnt = 1;
        while (q.size() > 0) {
            //print();
            if (cnt % k == 0) {
                int res = q.poll();
                System.out.print(res + " ");
            } else {
                int res = q.poll();
                q.add(res);
            }
            cnt += 1;
        }
    }
}