import java.util.Scanner;

public class Main {
    public static int[] dx = new int[]{-1, 0, 1, 0};
    public static int[] dy = new int[]{0, 1, 0, -1};

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
    
        int x = 0, y = 0;
        for (int i = 0; i < n; i++) {
            char dir = sc.next().charAt(0);
            int dist = sc.nextInt();

            if (dir == 'N') {
                x += dx[2] * dist;
                y += dy[2] * dist;
            } else if (dir == 'S') {
                x += dx[0] * dist;
                y += dy[0] * dist;
            } else if (dir == 'E') {
                x += dx[1] * dist;
                y += dy[1] * dist;
            } else if (dir == 'W') {
                x += dx[3] * dist;
                y += dy[3] * dist;
            }
        }

        System.out.println(y + " " + x);

    }
}