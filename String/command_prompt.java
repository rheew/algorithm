import java.util.*;

public class Main
{
	
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String first = sc.next();
		int arr[] = new int [first.length()];
		for(int i=1; i<N; i++) {
			String next = sc.next();
			for(int j=0; j<first.length(); j++) {
				if(next.charAt(j)!=first.charAt(j))arr[j]=1;
			}
		}
		for(int j=0; j<first.length(); j++) {
			if(arr[j]==0)
			System.out.print(first.charAt(j));
			else System.out.print("?");
		}
	}

}