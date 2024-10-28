import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int k = Integer.parseInt(br.readLine());

            TreeSet<Integer> s = new TreeSet<>();
            while (k-- > 0) {
                st = new StringTokenizer(br.readLine());

                String option = st.nextToken();

                if (option.equals("I")) {
                    int n = Integer.parseInt(st.nextToken());
                    s.add(n);
                } else if (option.equals("D")) {
                    int n = Integer.parseInt(st.nextToken());

                    if (n == 1) {
                        if (!s.isEmpty())
                            s.remove(s.last());
                    } else if (n == -1) {
                        if (!s.isEmpty())
                            s.remove(s.first());
                    }
                }
            }

            if (s.isEmpty()) {
                sb.append("EMPTY");
            } else {
                sb.append(s.last()).append(" ").append(s.first());
            }

            System.out.println(sb);
            sb.setLength(0);
        }


    }
}