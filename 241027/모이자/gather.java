import java.util.Scanner;

public class Main {
    public static int INT_MIN = Integer.MAX_VALUE;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
    
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int minVal = INT_MIN;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                int dist = Math.abs(i - j);

                sum += arr[j] * dist;
            }
            minVal = Math.min(minVal, sum);
        }

        System.out.println(minVal);
    }
}