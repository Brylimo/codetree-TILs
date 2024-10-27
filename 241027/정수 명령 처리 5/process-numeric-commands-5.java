import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ArrayList<Integer> array = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String order = sc.next();

            if (order.equals("push_back")) {
                int a = sc.nextInt();

                array.add(a);
            } else if (order.equals("pop_back")) {
                if (array.size() > 0) {
                    array.remove(array.size() - 1);
                }
            } else if (order.equals("size")) {
                System.out.println(array.size());
            } else if (order.equals("get")) {
                int idx = sc.nextInt();

                if (array.size() > idx - 1) {
                    System.out.println(array.get(idx - 1));
                }
            }
        }
    }
}