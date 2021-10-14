import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

class Solution {
    static boolean[] visit;

    public int solution(String numbers) {
        int answer = 0;
        visit = new boolean[numbers.length()];

        DFS(0, numbers, 2, new StringBuilder());
        return answer;
    }
    public static void DFS(int depth, String str, int len, StringBuilder newStr) {
        if (depth == len) {
            System.out.println(newStr.toString());
            return;
        }

        for (int i = 0 ; i < str.length(); i++) {
            if (visit[i]) continue;

            visit[i] = true;
            newStr.append(str.charAt(i));
            DFS(depth + 1, str, len, newStr);
            visit[i] = false;
            newStr.deleteCharAt(depth);
        }
    }
}

public class test {
    public static void main(String[] args) {
        String str = "123";

    }


}
