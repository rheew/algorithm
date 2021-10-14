import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class test1 {
    public static void main(String[] args) {

        Solution s = new Solution();
        int[] ans = s.solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500});
        for (int i : ans)
            System.out.println(i + " ");
    }


}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        ArrayList<Integer> ans = new ArrayList<>();
        HashMap<String, Integer> genreCnt = new HashMap<>();
        HashMap<String, ArrayList<genreList>> album = new HashMap<>();

        PriorityQueue<genre> pq = new PriorityQueue<>();

        for (int i = 0; i < genres.length; i++) {
            int cnt = genreCnt.getOrDefault(genres[i], 0);
            ArrayList<genreList> nowList = album.getOrDefault(genres[i], new ArrayList<genreList>());

            nowList.add(new genreList(plays[i], i));
            genreCnt.put(genres[i], plays[i] + cnt);
            album.put(genres[i], nowList);
        }

        for (String s : genreCnt.keySet()) {
            pq.add(new genre(genreCnt.get(s), s));
        }

        int counter = 2;
        while ( counter != 0 && !pq.isEmpty() ) {
            counter -= 1;

            genre now = pq.remove();
            System.out.println(now.name);
            ArrayList<genreList> nowList = album.get(now.name);

            Collections.sort(nowList);

            int temp = 2;
            for (genreList a : nowList) {
                if (temp == 0) break;
                temp--;
                ans.add(a.ind);
            }
        }

        System.out.println();

        return ans.stream().toArray();

    }

}

class genreList implements Comparable<genreList> {
    int ind;
    int total;

    genreList(int total, int ind){
        this.ind = ind;
        this.total = total;
    }

    @Override
    public int compareTo(genreList o1) {
        if (o1.total == this.total) {
            return this.ind - o1.ind;
        }
        return o1.total - this.total;
    }
}

class genre implements Comparable<genre>{
    int total;
    String name;

    genre(int total, String name) {
        this.total = total;
        this.name = name;
    }

    @Override
    public int compareTo(genre o1) {
        return o1.total - this.total;
    }
}
