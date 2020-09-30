import java.util.*;

public class Main
{
	
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		HashSet<String> hs = new HashSet<>();
		ArrayList<String> Al = new ArrayList<>();
		int N = sc.nextInt();
		int M = sc.nextInt();
		for(int i=0; i<N; i++) {
			hs.add(sc.next());
		}
		for(int i=0; i<M; i++) {
			String str = sc.next();
			if(hs.contains(str))Al.add(str);
		}
		Collections.sort(Al);
		System.out.println(Al.size());
		for(String i : Al)
			System.out.println(i);
		
		
	}

}