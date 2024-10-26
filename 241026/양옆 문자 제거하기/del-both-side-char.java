import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        System.out.println(str.substring(0, 2) + str.substring(3, str.length() - 2) + str.substring(str.length() - 1));
    
    }
}