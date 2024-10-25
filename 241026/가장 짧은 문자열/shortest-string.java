import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int a = sc.next().length();
        int b = sc.next().length();
        int c = sc.next().length();

        if (a >= b && b >= c) {
            System.out.println(a - c);
        } else if (a >= c && c >= b) {
            System.out.println(a - b);
        } else if (b >= a && a >= c) {
            System.out.println(b - c);
        } else if (b >= c && c >= a) {
            System.out.println(b - a);
        } else if (c >= a && a >= b) {
            System.out.println(c - b);
        } else if (c >= b && b >= a) {
            System.out.println(c - a);
        }
    }
}