import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class comp implements Comparator<node> {
	@Override
	public int compare(node o1, node o2) {
		if (o1.y == o2.y) {
			return o1.x - o2.x;
		}
		else {
			return o1.y - o2.y;	
		}
		
	}
}

class node{
	int x, y;
	node(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {
	static ArrayList<node> al;
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		al = new ArrayList<>();
		
		for (int i = 0; i < N; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			al.add(new node(a, b));
		}
		
		Collections.sort(al, new comp());
		
		for (node x : al) {
			System.out.println(x.x + " " + x.y);
		}
	}                                                      	
}
//class comp implements Comparator<String[]>{
//public int compare(String[] o1, String[] o2) {
//	return o1[1].compareTo(o2[1]);
//}
//}