import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Integer>[] tree;
    static int[] parent;
    static boolean[] visited;

    static void dfs(int root) {

        for (int node : tree[root]) {
            if (!visited[node]) {
                visited[node] = true;
                parent[node] = root;
                dfs(node);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        
        parent = new int[n+ 1];
        visited = new boolean[n + 1];
        tree = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            tree[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            tree[x].add(y);
            tree[y].add(x);
        }

        visited[1] = true;
        dfs(1);

        for (int i = 2; i <= n; i++) {
            System.out.println(parent[i]);
        }
    }
}