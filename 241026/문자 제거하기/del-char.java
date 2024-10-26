import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        while (true) {
            if (str.length() == 1) {
                break;
            }

            int idx = sc.nextInt();

            if (idx >= str.length() || idx == str.length() - 1) {
                idx = str.length() - 1;

                str = str.substring(0, idx);
            } else {
                str = str.substring(0, idx) + str.substring(idx + 1);
            }
            System.out.println(str);
        }
    
    }
}