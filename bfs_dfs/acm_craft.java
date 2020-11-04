import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int T=sc.nextInt();
		for(int l=0;l<T;l++) {
			int N=sc.nextInt();
			int M=sc.nextInt();
			int arr[][]=new int [N+1][2];
			int a,b,c,i,j;
			
			ArrayList<Integer>[] list=new ArrayList[N+1];
			Queue<Integer> q=new LinkedList<>();
			int ind[]=new int [N+1];
			for(i=1;i<=N;i++) {
				arr[i][0]=sc.nextInt();
				arr[i][1]=arr[i][0];
			}
			arr[1][1]=arr[1][0];
			for(i=1;i<=N;i++) {
				list[i]=new ArrayList<>();
			}
			for(i=0;i<M;i++) {
					a=sc.nextInt();
					b=sc.nextInt();
					list[a].add(b);
					ind[b]++;
			}
			int finish=sc.nextInt();
			
			for(i=1;i<=N;i++) {
				if(ind[i]==0)q.add(i);
			}
			
			while(!q.isEmpty()) {
				c=q.remove();
				//System.out.println(c+": 계산");
				for(i=0;i<list[c].size();i++) {
					int pick=list[c].get(i);
					ind[pick]--;
					//System.out.println(pick+"은");
					//System.out.print(arr[pick][1]+" "+arr[c][1]+" "+arr[pick][0]+" ");
					//System.out.println();
					arr[pick][1]=Math.max(arr[pick][1],arr[c][1]+arr[pick][0]);
					
					if(ind[pick]==0) {
						
						q.add(pick);
						
					}
				}
				
			}
			System.out.println(arr[finish][1]);
	
	
		}
	}
}