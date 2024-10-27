import java.util.*;

public class Main {
    public static int n, k;
    public static ArrayList<Integer> candidates = new ArrayList<>();

    public static void calculate(int current) {
        if (current == n) {
            for (int i = 0; i < candidates.size(); i++) {
                System.out.println(candidates.get(i));
            }
            return;
        }

        for (int i = 1; i <= k; i++) {
            if (candidates.size() >= 2 && candidates.get(candidates.size() - 1) == i && candidates.get(candidates.size() - 2) == i) continue;

            candidates.add(i);
            calculate(current + 1);
            candidates.remove(candidates.size() - 1);
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        k = sc.nextInt();
        n = sc.nextInt();

        calculate(0);
    }
}