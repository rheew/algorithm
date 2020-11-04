import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.*;

class node {
	int x, y;
	node(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {
	static String [][] board;
	static int dx[] = {0,0,1,-1};
	static int dy[] = {1,-1,0,0};
	static Queue<node> position = new LinkedList<>();
	
	public static void remove() {
		while (!position.isEmpty()) {
			node now = position.remove();
			board[now.x][now.y] = ".";
		}
		
		for (int i = 10; i >= 0; i--) {
			for (int j = 0 ; j < 6; j++) {
				if (board[i][j].equals(".")) continue;
				int ni = i;
				while (ni != 11 && board[ni+1][j].equals(".")) {
					ni += 1;
				}

				if (ni != i) {
					board[ni][j] = board[i][j];
					board[i][j] = ".";
				}
				
			}
		}
		
	}
	public static boolean BFS(int a, int b) {
		Queue<node> q = new LinkedList<>();
		Queue<node> pos = new LinkedList<>();
		boolean [][] visit = new boolean [12][6];
		
		String init = board[a][b];
		int cnt = 0;
		q.add(new node(a, b));	
		pos.add(new node(a, b));

		while (!q.isEmpty()) {
			node now = q.remove();
			
			for (int i = 0; i < 4; i++) {
				int nx = dx[i] + now.x;
				int ny = dy[i] + now.y;
				
				if (nx >= 12 || nx < 0 || ny >= 6 || ny < 0) continue;
				if (visit[nx][ny]) continue;
				if (init.equals(board[nx][ny])) {
					cnt += 1;
					visit[nx][ny] = true;
					q.add(new node(nx, ny));	
					pos.add(new node(nx, ny));
				}
				
			}
			
		}
		
		if (cnt > 3) {
			while (!pos.isEmpty()) {
				position.add(pos.remove());
			}
			
			return true;
		}
		
		return false;
	}
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		board = new String [12][6];
		
		int ans = 0;
		
		for (int i = 0; i < 12; i++) {
			board[i] = sc.nextLine().split("");
		}
		
		while(true) {
			
			for (int i = 0; i < 12; i++) {
				for (int j = 0; j < 6; j++) {
					if (board[i][j].equals(".")) continue;
					BFS(i, j);
				}
				
			}
			if (position.isEmpty()) break;
			else {
				ans += 1;
				remove();
			}
			
		}
		
		System.out.println(ans);
		
	}
}

//}
//}