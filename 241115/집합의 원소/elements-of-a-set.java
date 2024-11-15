import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 100000;

    public static int n, m;
    public static int[] parent;

    public static void union(int a, int b) {
        int parentA = find(a);
        int parentB = find(b);

        if (parentA < parentB) {
            parent[parentB] = parentA;
        } else {
            parent[parentA] = parentB;
        }
    }

    public static int find(int x) {
        if (x != parent[x])
            parent[x] = find(parent[x]);

        return parent[x];
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];

        // 초기화
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
        
            int op = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (op == 0) { // union
                union(a, b);
            } else { // find
                int parentA = find(a);
                int parentB = find(b);

                if (parentA == parentB) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            }
        }
    }
}