import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        char[] arr = new char[]{'L', 'E', 'B', 'R', 'O', 'S'};

        int index = -1;

        char target = sc.next().charAt(0);

        for (int i = 0; i < 6; i++) {
            if (arr[i] == target) {
                index = i;
                break;
            }
        }

        if (index == -1) {
            System.out.println("None");
        } else{
            System.out.println(index);
        }
    }
}