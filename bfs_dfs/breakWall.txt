import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class node{
	int x,y;
	boolean flag;
	node(int x, int y, boolean flag){
		this.x = x;
		this.y = y;
		this.flag = flag;
	}
}
public class Main {
	static String map[][];
	static int visit[][][];
	static int N, M;
	static int dx[] = {0,0,1,-1};
	static int dy[] = {1,-1,0,0};
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		map = new String[N][M];
		visit = new int [2][N][M];
		
		sc.nextLine();
		for(int i=0; i<N; i++) {
			map[i] = sc.nextLine().split("");
		}
		
		for(int arr[][] : visit) {
			for(int ar[] : arr) {
				Arrays.fill(ar, -1);
			}
		}
		
		visit[0][0][0] = 1;
		DFS(false, 0, 0);
		if(visit[0][N-1][M-1] == -1)System.out.println(visit[1][N-1][M-1]);
		else if(visit[1][N-1][M-1] == -1)System.out.println(visit[0][N-1][M-1]);
		else {
			System.out.println(Math.min(visit[1][N-1][M-1],visit[0][N-1][M-1]));
		}
		
	}
	public static void DFS(boolean flag, int x, int y) {
		Queue<node> q = new LinkedList<>();
		q.add(new node(x, y, flag));
		
		while(!q.isEmpty()) {
			
			node now = q.remove();
			if(now.x == N-1 && now.y == M-1)continue;
			for(int i=0; i<4; i++) {
				
				int nextx = now.x + dx[i];
				int nexty = now.y + dy[i];
				
				if((nextx < 0) || (nextx >= N) || (nexty >= M) || (nexty < 0))continue;
				if(!now.flag&&(visit[0][nextx][nexty] != -1) && (visit[0][now.x][now.y]+1 >= visit[0][nextx][nexty]))continue;
				if(now.flag&&(visit[1][nextx][nexty] != -1) && (visit[1][now.x][now.y]+1 >= visit[1][nextx][nexty]))continue;
				
				if(now.flag) {
					if(map[nextx][nexty].equals("1"))continue;
					else {
						visit[1][nextx][nexty] = visit[1][now.x][now.y]+1;
						q.add(new node(nextx, nexty, now.flag));
					}
				}
				else {
					if(map[nextx][nexty].equals("1")) {
						visit[1][nextx][nexty] = visit[0][now.x][now.y]+1;
						q.add(new node(nextx, nexty, true));
					}
					else {
						visit[0][nextx][nexty]= visit[0][now.x][now.y]+1;
						q.add(new node(nextx, nexty, now.flag));
					}
				}
			}
			
		}
	}
	                                                          	
}
