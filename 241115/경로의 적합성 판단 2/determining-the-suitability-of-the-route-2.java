import java.util.*;
import java.io.*;

public class Main {
    public static final int MAX_N = 100000;
    public static int[] parent = new int[MAX_N];

    public static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }

        return parent[x];
    }

    public static void union(int a, int b) {
        int parentA = find(a);
        int parentB = find(b);

        if (parentA < parentB) {
            parent[parentB] = parentA;
        } else {
            parent[parentA] = parentB;
        }
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            union(x, y);
        }

        st = new StringTokenizer(br.readLine());
        
        int current = 0;
        int x = Integer.parseInt(st.nextToken());
        current = find(x);

        int ans = 1;
        for (int i = 1; i < k; i++) {
            x = Integer.parseInt(st.nextToken());
            int group = find(x);

            if (current != group) {
                ans = 0;
                break;
            }
        }       

        System.out.println(ans);
    }
}