import java.util.*;

public class Main {
    public static int n, ans;
    public static ArrayList<Integer> candidates = new ArrayList<>();

    public static boolean check() {
        int idx = 0;
        while (idx < n) {
            int num = candidates.get(idx);

            if (idx + num <= n) {
                for (int j = idx + 1; j < idx + num; j++) {
                    if (candidates.get(j) != num) {
                        return false;
                    }
                }
                idx += num;
            } else {
                return false;
            }
        }

        return true;
    }

    public static void calculate(int current) {
        if (current == n) {
            if (check()) {
                ans += 1;
            }
            return;
        }

        for (int i = 1; i <= 4; i++) {
            candidates.add(i);
            calculate(current + 1);
            candidates.remove(candidates.size() - 1);
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        calculate(0);

        System.out.println(ans);
    }
}