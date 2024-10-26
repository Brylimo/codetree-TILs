import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        int l = str.length();

        for (int i = 0; i <= l; i++) {
            System.out.println(str);
            str = str.substring(str.length() - 1) + str.substring(0, str.length() - 1);
        }
    }
}