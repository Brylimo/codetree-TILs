import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        Stack<Integer> s = new Stack<>();
        for (int i = 0; i < n; i++) {
            String order = sc.next();

            if (order.equals("push")) {
                int a = sc.nextInt();
                s.push(a);
            } else if (order.equals("pop")) {
                int x = s.pop();
                System.out.println(x);
            } else if (order.equals("size")) {
                System.out.println(s.size());
            } else if (order.equals("empty")) {
                if (s.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if (order.equals("top")) {
                System.out.println(s.peek());
            }
        }
    }
}