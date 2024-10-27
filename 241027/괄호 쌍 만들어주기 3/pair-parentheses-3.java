import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        int cnt = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(') {
                for (int j = i + 1; j < str.length(); j++) {
                    if (str.charAt(j) == ')') {
                        cnt += 1;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}