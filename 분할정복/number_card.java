import java.util.*;

public class Main
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		HashSet<Integer> hs = new HashSet<>();
		int N = sc.nextInt();
		
		for(int i=0; i<N; i++) {
			hs.add(sc.nextInt());
		}
		int M =sc.nextInt();
		
		for(int i=0; i<M; i++) {
			if(hs.contains(sc.nextInt()))System.out.print(1+" ");
			else System.out.print(0+" ");
		}
	}
	


}