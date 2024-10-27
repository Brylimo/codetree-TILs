import java.util.*;

public class Main {
    public static final int MAX_N = 1001;
    public static int cnt;
    public static boolean[] visited = new boolean[MAX_N];
    public static ArrayList<Integer>[] graph = new ArrayList[MAX_N];
    
    public static void dfs(int vertex) {
        for (int i = 0; i < graph[vertex].size(); i++) {
            int current = graph[vertex].get(i);
            if (!visited[current]) {
                visited[current] = true;
                cnt += 1;
                dfs(current);
            }
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        for (int i = 0; i < MAX_N; i++) {
            graph[i] = new ArrayList<>();
        }

        while (m-- > 0) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            graph[x].add(y);
            graph[y].add(x); 
        }

        visited[1] = true;
        dfs(1);

        System.out.println(cnt);
    }
}