import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        HashSet<Integer> set = new HashSet<>();

        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());

            String option = st.nextToken();

            if (option.equals("add")) {
                int k = Integer.parseInt(st.nextToken());

                set.add(k);
            } else if (option.equals("remove")) {
                int k = Integer.parseInt(st.nextToken());

                set.remove(k);
            } else if (option.equals("find")) {
                int k = Integer.parseInt(st.nextToken());

                if (set.contains(k)) {
                    System.out.println("true");
                } else {
                    System.out.println("false");
                }
            }
        }
    }
}