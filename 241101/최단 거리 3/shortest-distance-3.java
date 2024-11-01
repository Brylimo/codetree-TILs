import java.util.*;
import java.io.*;

class Pair implements Comparable<Pair> {
    int x, v;

    public Pair(int x, int v) {
        this.x = x;
        this.v = v;
    }

    @Override
    public int compareTo(Pair pair) {
        return this.v - pair.v;
    }
}

public class Main {
    static final int MAX_N = 1000;
    static final int INT_MAX = Integer.MAX_VALUE;

    static ArrayList<Pair>[] graph = new ArrayList[MAX_N + 1];
    static int[] dist = new int[MAX_N + 1];
    static PriorityQueue<Pair> pq = new PriorityQueue<>();

    public static void dijkstra() {
        while (!pq.isEmpty()) {
            Pair pair = pq.poll();

            if (dist[pair.x] != pair.v) {
                continue;
            }

            for (Pair x : graph[pair.x]) {
                if (dist[x.x] > dist[pair.x] + x.v) {
                    dist[x.x] = dist[pair.x] + x.v;
                    pq.add(new Pair(x.x, dist[x.x]));

                    //System.out.println(Arrays.toString(dist));
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i <= n; i++) {
            dist[i] = INT_MAX;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int value = Integer.parseInt(st.nextToken());

            graph[a].add(new Pair(b, value));
            graph[b].add(new Pair(a, value));
        }

        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        dist[a] = 0;
        pq.add(new Pair(a, 0));
        
        dijkstra();

        System.out.println(dist[b]);
    }
}