import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[][] grid;
    static PriorityQueue<Pair> pq = new PriorityQueue<>();
    static int[] parent;

    public static int find(int x) {
        if (parent[x] == x) return x;

        return parent[x] = find(parent[x]);
    } 

    public static void union(int a, int b) {
        int parentA = find(a);
        int parentB = find(b);

        if (parentA < parentB) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            pq.add(new Pair(x, y, dist));
        }

        long sum = 0;
        while (!pq.isEmpty()) {
            Pair current = pq.poll();

            if (find(current.x) == find(current.y)) {
                continue;
            } else {
                union(current.x, current.y);
                sum += current.dist;
            }
        }

        System.out.println(sum);
    }

    static class Pair implements Comparable<Pair> {
        int x;
        int y;
        int dist;

        public Pair(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        @Override
        public int compareTo(Pair other) {
            return this.dist - other.dist;
        }
    }
}