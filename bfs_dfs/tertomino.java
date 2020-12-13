import java.util.Scanner;

public class Main {
	static int dx[]= {0,0,1,-1};
	static int dy[]= {1,-1,0,0};
	static int N,M;
	static int arr[][];
	public static void main(String []args) {
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		arr=new int [N][M];
		boolean visit[][]=new boolean[N][M];
		int max=0;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				arr[i][j]=sc.nextInt();
			}
		}
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
			max=Math.max(max,DFS(0,visit,i,j));
			if(i==0&&j==0||i==0&&j==M-1||i==N-1&&j==0||i==N-1&&j==M-1)continue;
			if(i==0) {
				max=Math.max(arr[i][j]+arr[i][j-1]+arr[i][j+1]+arr[i+1][j],max);
			}
			else if(i==N-1) {
				max=Math.max(arr[i][j]+arr[i][j-1]+arr[i][j+1]+arr[i-1][j],max);
			}
			else if(j==0) {
				max=Math.max(arr[i][j]+arr[i][j+1]+arr[i-1][j]+arr[i+1][j],max);
			}
			else if(j==M-1) {
				max=Math.max(arr[i][j]+arr[i][j-1]+arr[i-1][j]+arr[i+1][j],max);
			}
			else {
				max=Math.max(max, arr[i][j]+arr[i+1][j]+arr[i-1][j]+arr[i][j+1]+arr[i][j-1]-
				Math.min(arr[i][j-1],Math.min(arr[i-1][j],Math.min(arr[i+1][j],arr[i][j+1]))));
			}
			}
		}
		//왼쪽~ 오른쪽

//		boolean visit[][]=new boolean[N][M];
//		DFS(0,visit,0,0);
		System.out.println(max);
	}
	public static int DFS(int start,boolean visit[][],int x,int y) {
		if(start==4)return 0;
		int max=0;
		visit[x][y]=true;
		for(int i=0;i<4;i++) {
			if(x+dx[i]>=0&&y+dy[i]>=0&&x+dx[i]<N&&y+dy[i]<M) {
				if(!visit[x+dx[i]][y+dy[i]]) {
					max=Math.max(arr[x][y]+DFS(start+1,visit,x+dx[i],y+dy[i]),max);
				}
			}
		}
		visit[x][y]=false;
		return max;
	}

}


