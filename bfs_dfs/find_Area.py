import java.util.*;

class node {
    int x;
    int y;
    node(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class test {
    static int [][] board;
    static int [] dx = {0,0,1,-1};
    static int [] dy = {1,-1,0,0};
    static int N, M;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> answer = new ArrayList<>();

        N = sc.nextInt();
        M = sc.nextInt();
        int K = sc.nextInt();

        board = new int[N][M];


        for (int i=0; i<K; i++) {
            int sx = sc.nextInt();
            int sy = sc.nextInt();

            int ex = sc.nextInt();
            int ey = sc.nextInt();
            MakeArea(sx, sy, ex, ey);
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 1) continue;
                int num = BFS(i, j);
                answer.add(num);
            }
        }
        Collections.sort(answer);

        System.out.println(answer.size());

        for (int i : answer)
            System.out.print(i + " ");
    }

    public static void MakeArea(int sx, int sy, int ex, int ey) {

        for (int i = sy; i < ey; i++) {
            for (int j = sx; j < ex; j++) {
                board[i][j] = 1;
            }
        }

    }

    public static int BFS(int i, int j) {
        Queue<node> q = new LinkedList();

        q.add(new node(j, i));
        board[i][j] = 1;
        int sum = 1;

        while (!q.isEmpty()) {
            node now = q.remove();

            for (int k = 0; k < 4; k++) {
                int nexty = dy[k] + now.y;
                int nextx = dx[k] + now.x;

                if (nextx < 0 || nextx >= M || nexty < 0 || nexty >= N) continue;
                if (board[nexty][nextx] == 1) continue;
                sum++;
                board[nexty][nextx] = 1;
                q.add(new node(nextx, nexty));

            }
        }

        return sum;
    }
}
