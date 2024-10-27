import java.util.Scanner;

public class Main {
    public static int n, t, x, y, dir;
    public static int[][] grid;
    public static int[] dx = new int[]{-1, 0, 0, 1};
    public static int[] dy = new int[]{0, 1, -1, 0}; 

    public static boolean inRange(int x, int y) {
        return (1 <= x && x <= n && 1 <= y && y <= n);
    }

    public static void move() {
        
        for (int i = 0; i < t; i++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (!inRange(nx, ny)) {
                dir = (3 - dir) % 4;
                continue;
            }

            x = nx;
            y = ny;
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        t = sc.nextInt();

        int r = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.next().charAt(0);

        x = r;
        y = c;
        grid = new int[n + 1][n + 1];

        if (d == 'U') {
            dir = 0;
        } else if (d == 'D') {
            dir = 3;
        } else if (d == 'R') {
            dir = 1;
        } else {
            dir = 2;
        }

        move();

        System.out.println(x + " " + y);
    }
}