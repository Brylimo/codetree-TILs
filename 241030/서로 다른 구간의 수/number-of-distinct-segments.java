import java.util.*;
import java.io.*;

class Segment {
    int x, y;

    public Segment(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Point implements Comparable<Point> {
    int x, v, index;

    public Point(int x, int v, int index) {
        this.x = x;
        this.v = v;
        this.index = index;
    }

    @Override
    public int compareTo(Point p) {
        return this.x - p.x;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        ArrayList<Point> points = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            points.add(new Point(a, 1, i));
            points.add(new Point(b, -1, i));
        }

        Collections.sort(points);

        HashSet<Integer> set = new HashSet<>();

        int ans = 0;
        for (int i = 0; i < 2 * n; i++) {
            if (points.get(i).v == 1) {
                if (set.isEmpty()) {
                    ans += 1;
                }

                set.add(points.get(i).index);
            } else if (points.get(i).v == -1) {
                set.remove(points.get(i).index);
            }
        }

        System.out.println(ans);
    }
}