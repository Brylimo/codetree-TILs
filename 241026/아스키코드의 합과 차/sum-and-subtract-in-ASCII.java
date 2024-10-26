import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        char a, b;
        a = sc.next().charAt(0);
        b = sc.next().charAt(0);

        int sum = (int)a + (int)b;
        int subtract = (int)a - (int)b;

        if (subtract < 0) subtract *= -1;

        System.out.println(sum + " " + subtract); 
    
    }
}