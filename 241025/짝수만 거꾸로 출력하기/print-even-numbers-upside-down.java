import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int cnt = 0;
        int[] arr2 = new int[n];
        for (int i = 0; i < n; i++) {
            if (arr[i] % 2 == 0) {
                arr2[cnt] = arr[i];
                cnt += 1;
            }
        }

        for (int i = cnt - 1; i >= 0; i--) {
            System.out.print(arr2[i] + " ");
        }
    }
}