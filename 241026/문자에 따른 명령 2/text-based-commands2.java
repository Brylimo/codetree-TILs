import java.util.Scanner;

public class Main {
    public static int x, y, dir;
    public static int[] dx = new int[]{1, 0, -1, 0};
    public static int[] dy = new int[]{0, 1, 0, -1};
    
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        for (int i = 0; i < str.length(); i++) {
            char target = str.charAt(i);

            if (target == 'L') { // 왼쪽으로 회전
                dir = (dir - 1 + 4) % 4;
            } else if (target == 'R') { // 오른쪽으로 회전
                dir = (dir + 1) % 4;
            } else {
                x = x + dx[dir];
                y = y + dy[dir];
            }
        }

        System.out.println(y + " " + x);
    }
}