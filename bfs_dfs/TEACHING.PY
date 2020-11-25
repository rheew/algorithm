import java.util.Scanner;
public class Main {
//abcdefghijklnmopqrstuvwxyz
	static String str[];
	static int max;
		public static void main(String []args) {
			Scanner sc=new Scanner(System.in);
			int N=sc.nextInt();
			int M=sc.nextInt();
			char arr[]= {'b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z'};
			str=new String[N];
			for(int i=0;i<N;i++)
				str[i]=sc.next();
			if(M<5)
				System.out.println('0');
			else {
			DFS(0,M-5,arr,new char[M-5]);
			System.out.println(max);
			}
		}
		public static void DFS(int start,int k,char arr[],char arr1[]) {
			if(k==start) {
				boolean visit[]=new boolean[27];
				int temp=0,j;
				for(int i=0;i<start;i++)
					visit[arr1[i]-96]=true;
				visit['a'-96]=true;
				visit['n'-96]=true;
				visit['c'-96]=true;
				visit['t'-96]=true;
				visit['i'-96]=true;
				for(int i=0;i<str.length;i++) {
					for(j=0;j<str[i].length();j++) {
						if(visit[str[i].charAt(j)-96])continue;
						else break;
					}
					if(j>=str[i].length())temp++;
				}
				max=Math.max(max, temp);
				return;
			}
			for(int i=start;i<21;i++) {
				if(start>0)
				if(arr1[start-1]>=arr[i])continue;
				arr1[start]=arr[i];
				DFS(start+1,k,arr,arr1);
			}
		}
		public static void con() {

		}
		
 }


