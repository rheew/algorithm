import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

class node implements Comparable<node>{
    int ind;
    int time;

    public node(int ind, int time) {
        this.ind = ind;
        this.time = time;
    }

    @Override
    public int compareTo(node o) {
        if (this.time == o.time) {
            return this.ind - o.ind;
        }
        else return this.time - o.time;
    }
}

public class test {

    public static void main(String[] args) {
        int N = 3;
        int [] coffee_times = {100, 1, 50, 1, 1};

        int[] result = solution(N, coffee_times);

        System.out.println(Arrays.toString(result));
    }

    public static int[] solution (int N, int[] coffee_times) {
        int[] result = new int[coffee_times.length];
        int result_ind = 0;
        PriorityQueue<node> making = new PriorityQueue<>();
        PriorityQueue<node> making_after = new PriorityQueue<>();

        Queue<node> wait = new LinkedList<>();
        int ind = 0;

        for (int coffee_time : coffee_times)
            wait.add(new node(ind++, coffee_time));

        while (wait.size() != 0 || making.size() != 0) {

            //주문 접수
            while (wait.size() > 0 && N > making.size()) {
                node now = wait.remove();
                making.add(now);
            }


            node min_time = making.remove();
            result[result_ind++] = min_time.ind + 1;
            int len = making.size();

            for (int i = 0; i < len; i++) {

                node now = making.remove();
                if (now.time == min_time.time) {
                    result[result_ind++] = now.ind + 1;
                }
                else {
                    making_after.add(new node(now.ind, now.time - min_time.time));
                }
            }

            len = making_after.size();
            for (int i = 0; i < len; i++) {
                making.add(making_after.remove());
            }

        }
        
        return  result;
    }
}
