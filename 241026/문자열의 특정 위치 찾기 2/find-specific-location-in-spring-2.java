import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        char target = sc.next().charAt(0);

        String[] array = new String[]{ "apple", "banana", "grape", "blueberry", "orange" };

        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (array[i].charAt(2) == target || array[i].charAt(3) == target) {
                System.out.println(array[i]);
                cnt += 1;
            }
        }

        System.out.println(cnt);
    }
}