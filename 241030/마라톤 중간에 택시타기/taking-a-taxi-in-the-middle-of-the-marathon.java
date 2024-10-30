import java.util.*;
import java.io.*;

class Pair {
    int x, y;
    public Pair (int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static final int INT_MAX = Integer.MAX_VALUE;
    static final int MAX_N = 100000;

    static Pair[] course = new Pair[MAX_N];

    static int distance(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            course[i] = new Pair(x, y);
        }

        int[] L = new int[n];
        int[] R = new int[n];

        // L 초기화
        for (int i = 1; i < n; i++) {
            L[i] = L[i - 1] + distance(course[i - 1].x, course[i - 1].y, course[i].x, course[i].y);
        }

        // R 초기화
        for (int i = n - 2; i >= 0; i--) {
            R[i] = R[i + 1] + distance(course[i + 1].x, course[i + 1].y, course[i].x, course[i].y);
        }

        int minVal = INT_MAX;
        for (int i = 1; i < n - 1; i++) {
            int dist = L[i - 1] + R[i + 1] + distance(course[i - 1].x, course[i - 1].y, course[i + 1].x, course[i + 1].y);
            minVal = Math.min(minVal, dist);
        }

        System.out.println(minVal);
    }
}