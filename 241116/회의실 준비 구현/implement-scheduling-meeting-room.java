import java.util.*;
import java.io.*;

public class Main {
    static class Pair implements Comparable<Pair> {
        int start, end;

        public Pair(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Pair pair) {
            return this.end - pair.end;
        }
    }
    
    public static ArrayList<Pair> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            list.add(new Pair(start, end));
        }

        Collections.sort(list);

        int temp = 0;
        int ans = 0;
        for (Pair pair : list) {
            if (temp <= pair.start) {
                temp = pair.end;
                ans += 1;
            }
        }

        System.out.println(ans);
    }
}