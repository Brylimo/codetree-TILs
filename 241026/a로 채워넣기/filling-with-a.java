import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        char[] arr = str.toCharArray();

        arr[1] = 'a';
        int idx = arr.length - 2;
        arr[idx] = 'a';
    
        String newStr = String.valueOf(arr);

        System.out.println(newStr);
    }
}