import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        char[] array = str.toCharArray();
        Arrays.sort(array);

        System.out.println(String.valueOf(array));
    }
}