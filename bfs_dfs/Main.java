import java.io.*;
import java.util.*;
public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		Queue<Integer> q =new LinkedList<>();
		int answer = 0;
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int node[][] = new int[N][N];
		boolean visit[] = new boolean[N];
		
		for(int i=0; i<M; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			node[a-1][b-1] = 1;
			node[b-1][a-1] = 1;
		}
		
		q.add(0);
		visit[0] = true;
		while(!q.isEmpty()) {
			int value = q.remove();
			
			for(int i=0; i<N; i++) {
				if(visit[i]||node[value][i] == 0)continue;
				visit[i] = true;
				q.add(i);
				answer++;
			}
		}
		System.out.println(answer);
		
	}
	
	
	
}
