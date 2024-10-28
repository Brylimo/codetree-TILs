import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        
        int n = sc.nextInt();
        int[] arr1 = new int[n];
        HashSet<Integer> h1 = new HashSet<>();

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            arr1[i] = x;
            h1.add(x);
        }

        int m = sc.nextInt();
        int[] arr2 = new int[m];
        HashSet<Integer> h2 = new HashSet<>();
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            arr2[i] = x;
            h2.add(x);
        }

        for (int i = 0; i < m; i++) {
            if (h1.contains(arr2[i])) {
                sb.append("1").append(" ");
            } else {
                sb.append("0").append(" ");
            }
        }
     
        System.out.println(sb);
    }
}