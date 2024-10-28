import java.util.*;
import java.io.*;

class Pair implements Comparable<Pair> {
    int x, y;

    public Pair (int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Pair pair) {
        int tDist = Math.abs(this.x) + Math.abs(this.y);
        int cDist = Math.abs(pair.x) + Math.abs(pair.y);

        if (tDist != cDist) {
            return tDist - cDist;
        }
        if (this.x != pair.x) {
            return this.x - pair.x;
        }

        return this.y - pair.y;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        PriorityQueue<Pair> pq = new PriorityQueue<>();
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            pq.add(new Pair(x, y));
        }

        while (m-- > 0) {
            Pair res = pq.poll();

            pq.add(new Pair(res.x + 2, res.y + 2));
        }

        Pair res = pq.poll();
        System.out.println(res.x + " " + res.y);
    }
}