import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static boolean change(int num[], int i, int j) {
		if (num[i] > num[j]) {
			int temp = num[i];
			num[i] = num[j];
			num[j] = temp;
			for (int a=0; a<5; a++) {
				System.out.print(num[a] + " ");
					
			}
			System.out.println();
			return true;
		}
		return false;
	}
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int num[] = new int [5];
		
		for (int i=0; i<5; i++) {
			num[i] = sc.nextInt();
		}
		
		boolean flag = false;
		
		while (!flag) {
			flag = true;
			for (int i=0; i<4; i++) {
				if(change(num, i, i+1)) flag = false;
			}
		}
		
	}                                                      	
}