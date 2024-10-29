import java.util.*;
import java.io.*;

public class Main {
    public static final int INT_MIN = Integer.MIN_VALUE;
    public static final int MAX_N = 100000;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] arr = new int[MAX_N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        TreeSet<Integer> t = new TreeSet<>();
        HashMap<Integer, Integer> mapper = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            t.add(arr[i]);
        }

        int cnt = 0;
        for (int item : t) {
            mapper.put(item, cnt);
            cnt += 1;
        }

        while (q-- > 0) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int left = INT_MIN, right = INT_MIN;
            if (t.ceiling(a) != null) {
                left = t.ceiling(a); 
            }
            if (t.floor(b) != null) {
                right = t.floor(b);
            }

            left = mapper.get(left);
            right = mapper.get(right);

            if (left == INT_MIN || right == INT_MIN) {
                System.out.println(0);
            } else {
                            System.out.println(right - left + 1);
            }
        }
    }
}