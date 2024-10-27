import java.util.*;

public class Main {
    public static final int MAX_N = 8;
    public static int n;

    public static boolean[] visited = new boolean[MAX_N + 1];
    public static ArrayList<Integer> candidates = new ArrayList<>();

    public static void calculate(int current) {
        if (current == n) {
            for (int i = 0; i < n; i++) {
                System.out.print(candidates.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            candidates.add(i);

            calculate(current + 1);

            candidates.remove(candidates.size() - 1);
            visited[i] = false;
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        
        calculate(0);
    }
}