class Solution {
    static int[][] answer;
    static int temp = 0;
  public int[][] solution(int n) {
      answer = new int[(int)Math.pow(2,n)-1][2];
      top(n,1,2,3);
      return answer;
  }
    static void move(int from, int to){
        answer[temp][0] = from;
        answer[temp++][1] = to;
    }
    static void top(int n, int from, int by, int to){
        if(n == 1)move(from, to);
        else{
            top(n-1, from, to, by);
            move(from, to);
            top(n-1, by, from, to);
        }
    }
}