import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int sum = 0;
        for (int i = 0; i < 10; i++) {
            String str = sc.next();

            sum += str.length();
        }
    
        System.out.println(sum);
    }
}