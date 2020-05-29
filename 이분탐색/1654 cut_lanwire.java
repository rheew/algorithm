import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class Main {
	static long arr[];
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		arr = new long [N];
		
		for(int i=0; i<N; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);
		System.out.println(binarySearch(N, M, 1, arr[N-1]+1));
	}
	public static long binarySearch(int N , int M, long start, long end) {

		long sum = 0;
		long max = 0;
		while(start < end) {
			sum = 0;
			long mid = (start + end) / 2;
			
			for(int i=0; i<N; i++) {
				if(sum > M)break;
				sum += arr[i]/mid;
			}
			
			if(sum >= M) {
				start = mid + 1;
			}
			else {
				end = mid;
			}
		}
		
		return start - 1;
	}
	
	
}
