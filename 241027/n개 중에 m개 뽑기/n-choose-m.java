import java.util.*;

public class Main {
    public static int n, m;
    public static ArrayList<Integer> candidates = new ArrayList<>();
    
    public static void calculate(int idx, int cnt) {
        if (cnt == m) {
            for (int i = 0; i < candidates.size(); i++) {
                System.out.print(candidates.get(i) + " ");
            }
            System.out.println();
            return;
        }

        if (idx == n + 1) {
            if (cnt == m) {
                for (int i = 0; i < candidates.size(); i++) {
                    System.out.print(candidates.get(i) + " ");
                }
                System.out.println();
            }
            return;
        }

        candidates.add(idx);
        calculate(idx + 1, cnt + 1);
        candidates.remove(candidates.size() - 1);

        calculate(idx + 1, cnt);

    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        calculate(1, 0);
    
    }
}