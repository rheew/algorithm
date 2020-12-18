import java.util.*;

public class Main {
    static int N, ans;
    static ArrayList<Integer> al;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        al = new ArrayList<>();
        ans = 0;
        for (int i = 0; i < N; i++) {
            al.add(sc.nextInt());
        }
        DFS(new int[N], 0, new boolean[N]);
        System.out.println(ans);
    }
    public static void calculate(int ind[]) {
        ArrayList<Integer> sums = new ArrayList<>();
        int total = 0;

        for (int i = 0; i < N - 1; i++) {
            int sum = al.get(ind[i]) - al.get(ind[i + 1]);
            sums.add(Math.abs(sum));
        }

        for (int i = 0; i < N - 1; i++) {
            total += sums.get(i);
        }
        ans = Math.max(ans, total);
        return;
    }

    public static void DFS(int ind[], int temp, boolean visit[]) {
        if (temp == N) {
            calculate(ind);
            return;
        }

        for (int i = 0; i < N; i++) {
            if (visit[i]) continue;
            visit[i] = true;
            ind[temp] = i;
            DFS(ind, temp + 1, visit);
            visit[i] = false;
        }
    }
}
