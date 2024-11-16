import java.util.*;
import java.io.*;

public class Main {
    static class Pair implements Comparable<Pair> {
        int w, v;
        double cost;

        public Pair(int w, int v) {
            this.w = w;
            this.v = v;
            this.cost = (double)v / w;
        }

        @Override
        public int compareTo(Pair p) {
            return Double.compare(p.cost, this.cost);
        }
    }

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Pair[] array = new Pair[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            array[i] = new Pair(w, v);
        }

        Arrays.sort(array);

        double ans = 0;
        for (int i = 0; i < n; i++) {
            Pair current = array[i];

            if (current.w <= m) {
                m -= current.w;
                ans += current.v;
            } else {
                ans += current.cost * m;
                break;
            }
        }

        System.out.printf("%.3f", ans);
    }
}