import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = sc.nextInt();
        }

        int max_val = Integer.MIN_VALUE;
        for (int i = 0; i < 10; i++) {
            if (max_val < arr[i]) {
                max_val = arr[i];
            }
        }

        System.out.println(max_val);
    }
}