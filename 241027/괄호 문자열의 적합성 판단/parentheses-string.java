import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(ir);

        String str = br.readLine();
        Stack<Character> s = new Stack<>();

        char[] array = str.toCharArray();

        boolean flag = true;
        for (char piece : array) {
            if (s.isEmpty()) {
                if (piece == ')') {
                    flag = false;
                    break;
                } else {
                    s.push(piece);
                }
            } else {
                if (piece == '(') {
                    s.push(piece);
                } else {
                    char res = s.pop();

                    if (res != '(') {
                        flag = false;
                        break;
                    }
                }
            }
        }

        if (!s.isEmpty()) {
            flag = false;
        }

        if (flag) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}