import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        LinkedList<Integer> l = new LinkedList<>();
        while (n-- > 0){
            String order = sc.next();

            if (order.equals("push_front")) {
                int a = sc.nextInt();

                l.addFirst(a);
            } else if (order.equals("push_back")) {
                int a = sc.nextInt();

                l.addLast(a);
            } else if (order.equals("pop_front")) {
                int res = l.pollFirst();
                System.out.println(res);
            } else if (order.equals("pop_back")) {
                int res = l.pollLast();
                System.out.println(res);
            } else if (order.equals("size")) {
                System.out.println(l.size());
            } else if (order.equals("empty")) {
                if (l.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if (order.equals("front")) {
                System.out.println(l.peekFirst());
            } else if (order.equals("back")) {
                System.out.println(l.peekLast());
            }
        }
    
    }
}