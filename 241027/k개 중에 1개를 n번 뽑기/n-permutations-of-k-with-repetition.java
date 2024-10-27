import java.util.*;

public class Main {
    public static int k, n;
    public static ArrayList<Integer> candidate = new ArrayList<>();

    public static void calculate(int index) {
        if (index == n + 1) {
            for (int i = 0; i < n; i++) {
                System.out.print(candidate.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= k; i++) {
            candidate.add(i);
            calculate(index + 1);
            candidate.remove(candidate.size() - 1);
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        k = sc.nextInt();
        n = sc.nextInt();

        calculate(1);
    }
}