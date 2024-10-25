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

        final int INT_MAX = Integer.MAX_VALUE;
        int min_val = INT_MAX;

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (min_val > arr[i]) {
                min_val = arr[i];
                count = 1;
            } else if (min_val == arr[i]) {
                count += 1;
            }
        }

        System.out.println(min_val + " " + count);
    }
}