class Solution {
    static boolean visit[];
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visit = new boolean[n];

        for(int i =0; i<n; i++){
            if(visit[i])continue;
            visit[i]=true;
            network(computers, i);
            answer++;
        }
        return answer;
    }
    public static void network(int computers[][], int v){
        for(int i=0; i<computers[v].length; i++){
            if(visit[i]||computers[v][i]==0)continue;
                visit[i] = true;
                network(computers, i);
        }
    }
}