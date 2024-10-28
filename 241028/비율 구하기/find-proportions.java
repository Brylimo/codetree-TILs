import java.util.*;
import java.util.Map.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);

        TreeMap<String, Integer> m = new TreeMap<>();
        int n = Integer.parseInt(br.readLine());

        int total = 0;
        for (int i = 0; i < n; i++) {
            String key = br.readLine();

            if (m.containsKey(key)) {
                m.put(key, m.get(key) + 1);
            } else {
                m.put(key, 1);
            }

            total += 1;
        }

        Iterator<Entry<String, Integer>> i = m.entrySet().iterator();

        while (i.hasNext()) {
            Entry<String, Integer> entry = i.next();
            System.out.printf("%s %.4f\n", entry.getKey(), (entry.getValue() * 100 / (double)total));
        } 
    }
}