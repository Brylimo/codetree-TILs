import java.util.*;
import java.io.*;

class Point implements Comparable<Point> {
    int x, v;

    public Point(int x, int v) {
        this.x = x;
        this.v = v;
    }

    @Override
    public int compareTo(Point p) {
        return this.x - p.x;
    }
}

public class Main {
    public static final int MAX_N = 100000;

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        ArrayList<Point> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());

            points.add(new Point(x1, 1));
            points.add(new Point(x2, -1));
        }

        Collections.sort(points);

        int ans = 0;
        int sum = 0;
        for (int i = 0; i < points.size(); i++) {
            sum += points.get(i).v;
            ans = Math.max(ans, sum);
        }

        System.out.println(ans);
    }
}