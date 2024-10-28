import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        TreeSet<Integer> s = new TreeSet<>();
        TreeSet<Integer> dist = new TreeSet<>();

        // 처음에는 0만 존재
        s.add(0);

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        while (n-- > 0) {
            int x = Integer.parseInt(st.nextToken());

            s.add(x);

            if (s.higher(x) != null) {
                dist.add(s.higher(x) - x);
            }
            if (s.lower(x) != null) {
                dist.add(x - s.lower(x));
            }

            System.out.println(dist.first());
        }
    
    }
}