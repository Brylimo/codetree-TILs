import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();

        String first = a, second = b;
        for (int i = 0; i < a.length(); i++) {
            if (!('0' <= a.charAt(i) && a.charAt(i) <= '9')) {
                first = a.substring(0, i);
                break;
            }
        }

        for (int i = 0; i < b.length(); i++) {
            if (!('0' <= b.charAt(i) && b.charAt(i) <= '9')) {
                second = b.substring(0, i);
                break;
            }
        }

        System.out.println(Integer.parseInt(first) + Integer.parseInt(second));
    
    }
}