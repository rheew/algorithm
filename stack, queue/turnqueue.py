import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Deque<Integer> deque = new ArrayDeque<>();
		Deque<Integer> deque1 = new ArrayDeque<>();
		Iterator<Integer> iter;
		Queue<Integer> q = new LinkedList<>();
		int N = sc.nextInt();
		int M = sc.nextInt();
		for(int i=0; i<N; i++) {
			deque.add(i+1);
		}
		
		for(int i=0; i<M; i++)
			q.add(sc.nextInt());
		
		int find_value;
		int ans = 0;
		while(!q.isEmpty()) {
			int index = 0;
			find_value = q.remove();
			iter = deque.iterator();
			
			
				
				while(iter.hasNext()) {
				index++;
				if(iter.next() == find_value)break;
			}

			if(index > deque.size()/2+1 ? true : false) {
				ans++;
				int cnt = deque.removeLast();
				while(find_value != cnt) {
					deque.addFirst(cnt);
					cnt = deque.removeLast();
					ans++;
				}
				
				
			}
			else {
				int cnt = deque.removeFirst();
				while(find_value != cnt) {
					deque.addLast(cnt);
					cnt = deque.removeFirst();
					ans++;
				}
				
			}
			
			
		}
		System.out.println(ans);
	}

}
