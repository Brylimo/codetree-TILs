import java.util.*;
import java.io.*;

public class Main {
    static int n, cnt, rt = -1;
    static int[] parent;
    static boolean[] visited;
    static ArrayList<Integer>[] edges;

    static void dfs(int root) {
        if (edges[root].size() == 0) {
            if (root != rt) {
                cnt++;
            }
        }
        
        for (int node : edges[root]) {
            if (!visited[node]) {
                visited[node] = true;
                dfs(node);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        parent = new int[n];
        visited = new boolean[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            parent[i] = Integer.parseInt(st.nextToken());
        }

        int dNode = Integer.parseInt(br.readLine());

        edges = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            edges[i] = new ArrayList<>();
        }

        for (int i = 0; i < n; i++) {
            int pNode = parent[i];

            if (pNode == -1) {
                rt = i;
                continue;   
            }

            if (pNode != dNode && i != dNode) {
                edges[pNode].add(i);
            }
        }

        visited[rt] = true;
        dfs(rt);

        System.out.println(cnt);
    }
}