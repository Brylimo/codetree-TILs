import java.util.*;
import java.io.*;
import java.util.Map.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;
        TreeMap<Integer, Integer> m = new TreeMap<>();

        int n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            String option = st.nextToken();

            if (option.equals("add")) {
                int k = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());

                m.put(k, v);
            } else if (option.equals("remove")) {
                int k = Integer.parseInt(st.nextToken());
                m.remove(k);
            } else if (option.equals("find")) {
                int k = Integer.parseInt(st.nextToken());
                if (m.containsKey(k)) {
                    System.out.println(m.get(k));
                } else {
                    System.out.println("None");
                }
            } else if (option.equals("print_list")) {
                if (m.isEmpty()) {
                    System.out.println("None");
                } else {
                    Iterator<Entry<Integer, Integer>> i = m.entrySet().iterator();

                    while (i.hasNext()) {
                        int key = i.next().getKey();

                        System.out.print(m.get(key) + " ");
                    }
                    System.out.println();
                }
            }
        }
    }
}