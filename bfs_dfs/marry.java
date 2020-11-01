import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class node {
	int a, b;
	node(int a, int b) {
		this.a = a;
		this.b = b;
	}
}
public class Main {
	static ArrayList<ArrayList<Integer>> ver;
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		ver = new ArrayList<>();
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		for (int i = 0; i <= N; i++) {
			ver.add(new ArrayList());
		}
		
		for (int i = 0; i < M; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			ver.get(a).add(b);
			ver.get(b).add(a);
		}
		int answer = BFS(1, N);
		System.out.println(answer);
		
	}
	
	public static int BFS(int start, int N) {
		Queue<node> q = new LinkedList<>();
		boolean visit[] = new boolean [ N + 1 ];
		
		q.add(new node(start, 1));
		visit[start] = true;
		int cnt = 0;
		
		while (!q.isEmpty()) {
			node now = q.remove();
			
			if (now.b == 3) continue;
			
			for (int i=0; i<ver.get(now.a).size(); i++) {
				int next = ver.get(now.a).get(i);
				if (visit[next]) continue;

				cnt++;
				visit[next] = true;
				q.add(new node(next, now.b + 1));
			}
			
		}
		
		return cnt;
	}
	
	
	                                                          	
}