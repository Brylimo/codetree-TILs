import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        while(true) {
            String txt = sc.next();

            if (txt.equals("END")) break;

            for (int i = txt.length() - 1; i >= 0; i--) {
                System.out.print(txt.charAt(i));
            }
            System.out.println();
        }
    
    }
}