import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
    
        String str = sc.next();
        char target = sc.next().charAt(0);

        int result = str.indexOf(target);

        if (result == -1) {
            System.out.print("No");
        } else {
            System.out.print(result);
        }
    }
}