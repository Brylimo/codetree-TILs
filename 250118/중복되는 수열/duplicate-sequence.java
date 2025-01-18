import java.util.*;
import java.io.*;

public class Main {
    static TrieNode root = new TrieNode();
    static boolean[] visited;

    static void insertWord(String s) {
        TrieNode t = root;

        for (int i = 0; i < s.length(); i++) {
            int index = s.charAt(i) - '0';
            if (t.children[index] == null) {
                t.children[index] = new TrieNode();
            }

            t = t.children[index];
        }
        t.isEnd = true;
    }

    static boolean searchWord(String s) {
        TrieNode t = root;

        for (int i = 0; i < s.length(); i++) {
            if (t.isEnd) {
                return true;
            }

            int index = s.charAt(i) - '0';
            t = t.children[index];
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String[] lines = new String[n];
        for (int i = 0; i < n; i++) {
            lines[i] = br.readLine();
            insertWord(lines[i]);
        }

        boolean flag = false;
        for (int i = 0; i < n; i++) {
            if (searchWord(lines[i])) {
                flag = true;
                break;
            } else {
                flag = false;
            }
        }

        if (flag) {
            System.out.println(0);
        } else {
            System.out.println(1);
        }
    }

    static class TrieNode {
        boolean isEnd;
        TrieNode[] children = new TrieNode[10];

        TrieNode () {
            isEnd = false;

            for (int i = 0; i < 10; i++) {
                children[i] = null;
            }
        }
    }
}