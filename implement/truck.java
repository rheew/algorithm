import java.util.*;
class node {
    int wei;
    int time;
    node(int w, int t){
        this.wei = w;
        this.time = t;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> wait = new LinkedList<>();
        Queue<node> process = new LinkedList<>();

        int N = sc.nextInt();
        int L = sc.nextInt();
        int W = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int truck = sc.nextInt();
            wait.add(truck);
        }

        int totalWeight = 0;
        int totalTime = 0;

        while(!wait.isEmpty() || !process.isEmpty()) {
            totalTime += 1;

            int prosize = process.size();
            for (int i = 0; i < prosize; i++) {
                node truck = process.remove();
                if (truck.time != L) {
                    process.add(new node(truck.wei, truck.time + 1));
                }
                else {
                    totalWeight -= truck.wei;
                }
            }

            if (wait.size() > 0 && wait.peek() + totalWeight <= W){
                int truck = wait.remove();
                process.add(new node(truck, 1));
                totalWeight += truck;
            }
            
        }

        System.out.println(totalTime);
    }

}
