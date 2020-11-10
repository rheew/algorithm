import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class Main {
	static boolean[][] visit;
	static int[][] arr;
	static int N,M,V,i,j,Answer;
	static int[] x= {0,1,0,-1};
	static int[] y= {1,0,-1,0};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t=sc.nextInt();
		for(int w=0;w<t;w++) {
		N=sc.nextInt();
		M=sc.nextInt();
		V=sc.nextInt();
		arr=new int[N+1][M+1];
		visit=new boolean[N+1][M+1];
		Answer=0;
		int a,b;
			for(i=0;i<V;i++) {
			a=sc.nextInt();
			b=sc.nextInt();
			arr[a][b]=1;
			}
				for(i=0;i<N;i++)
					for(j=0;j<M;j++)
						if(arr[i][j]==1&&!visit[i][j]) {
							Answer++;
							DFS(i,j);
						}
				System.out.println(Answer);
		}
	}
	public static void DFS(int a,int b) {
		visit[a][b]=true;
		int z;
		for(z=0;z<4;z++) {
			if(a+x[z]>=0&&b+y[z]>=0&&a+x[z]<N&&b+y[z]<M)
			if(arr[a+x[z]][b+y[z]]==1&&!visit[a+x[z]][b+y[z]]) {
				DFS(a+x[z],b+y[z]);
			}
		}
			
	}

	
}