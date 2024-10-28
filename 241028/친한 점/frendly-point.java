import java.util.*;
import java.io.*;

class Pair implements Comparable<Pair> {
    int x, y;
    
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Pair pair) {
        if (this.x != pair.x) {
            return this.x - pair.x;
        }

        return this.y - pair.y;
    }

}

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Pair> s = new TreeSet<>();
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            int ax = Integer.parseInt(st.nextToken());
            int ay = Integer.parseInt(st.nextToken());

            s.add(new Pair(ax, ay));
        }

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            int bx = Integer.parseInt(st.nextToken());
            int by = Integer.parseInt(st.nextToken());

            Pair res = s.ceiling(new Pair(bx, by));
            if (res == null) {
                System.out.println(-1 + " " + -1);
            } else {
                System.out.println(res.x + " " + res.y);
            }
        }
    
    }
}