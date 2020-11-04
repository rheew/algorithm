import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		Set<String> s = new HashSet<>();
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		int ans = 0;
		sc.nextLine();
		
		for(int i=0; i<N; i++) {
			String input = sc.nextLine();
			s.add(input);
		}
		
		for (int i = 0; i < M; i++) {
			String input = sc.nextLine();
			if (s.contains(input)) {
				ans += 1;
			}
		}
		System.out.println(ans);
	}

}