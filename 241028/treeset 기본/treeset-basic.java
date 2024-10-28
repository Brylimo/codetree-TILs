import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        TreeSet<Integer> s = new TreeSet<>();

        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());

            String option = st.nextToken();

            if (option.equals("add")) {
                int x = Integer.parseInt(st.nextToken());

                s.add(x);
            } else if (option.equals("remove")) {
                int x = Integer.parseInt(st.nextToken());

                s.remove(x);
            } else if (option.equals("find")) {
                int x = Integer.parseInt(st.nextToken());

                if (s.contains(x)) {
                    System.out.println("true");
                } else {
                    System.out.println("false");
                }
            } else if (option.equals("lower_bound")) {
                int x = Integer.parseInt(st.nextToken());
                
                Integer e = s.ceiling(x);
                if (e == null) {
                    System.out.println("None");
                } else {
                    System.out.println(e);
                }
            } else if (option.equals("upper_bound")) {
                int x = Integer.parseInt(st.nextToken());
                
                Integer e = s.higher(x);
                if (e == null) {
                    System.out.println("None");
                } else {
                    System.out.println(e);
                }
            } else if (option.equals("largest")) {
                if (s.isEmpty()) {
                    System.out.println("None");
                } else {
                    System.out.println(s.last());
                }
            } else if (option.equals("smallest")) {
                if (s.isEmpty()) {
                    System.out.println("None");
                } else {
                    System.out.println(s.first());
                }
            }
        }

    }
}