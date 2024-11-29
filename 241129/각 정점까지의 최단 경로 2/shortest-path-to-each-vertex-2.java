import java.util.*;
import java.io.*;

public class Main {
    static class Edge {
        int s, e, v;

        public Edge(int s, int e, int v) {
            this.s = s;
            this.e = e;
            this.v = v;
        }
    }

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int INT_MAX = Integer.MAX_VALUE;

        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<Edge> edges = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            edges.add(new Edge(s, e, v));
        }

        long[][] dist = new long[n + 1][n + 1];
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < n + 1; j++) {
                dist[i][j] = INT_MAX;
            
                if (i == j) {
                    dist[i][j] = 0L;
                }
            }
        }

        for (Edge e : edges) {
            dist[e.s][e.e] = Math.min(dist[e.s][e.e], e.v);
        }

        for (int k = 1; k < n + 1; k++) {
            for (int i = 1; i < n + 1; i++) {
                for (int j = 1; j < n + 1; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        StringBuffer sb = new StringBuffer();
        for (int i = 1; i < n +1; i++) {
            for (int j = 1; j < n + 1; j++) {
                long ans = dist[i][j] >= INT_MAX ? -1L : dist[i][j];
                sb.append(ans).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}