import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();

        int sum = Integer.parseInt(a + b) + Integer.parseInt(b + a);

        System.out.println(sum);
    
    }
}