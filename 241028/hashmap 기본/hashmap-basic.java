import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        HashMap<Integer, Integer> map = new HashMap<>();

        int n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());

            String option = st.nextToken();

            int k = Integer.parseInt(st.nextToken());
            if (option.equals("add")) {
                int v = Integer.parseInt(st.nextToken());

                map.put(k, v);
            } else if (option.equals("remove")) {
                map.remove(k);
            } else if (option.equals("find")) {
                if (map.containsKey(k)) {
                    System.out.println(map.get(k));
                } else {
                    System.out.println("None");
                }
            }
        }

    
    }
}