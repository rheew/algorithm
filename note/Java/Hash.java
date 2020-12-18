vimport java.util.HashMap;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> m=new HashMap<>();
        for(int i=0;i<completion.length;i++){
            String str=completion[i];
            if(m.containsKey(str))
                m.put(str,m.get(str)+1);
            else m.put(str,1);
        }
        for(int i=0;i<participant.length;i++){
            String str=participant[i];
            if(m.containsKey(str)&&m.get(str)>0)m.put(str,m.get(str)-1);
            else answer=participant[i];
        }

        return answer;
    }
}

// hm.getOrDefault(player, 0) 디폴트 값을 설정해주는 함수
// hm.keySet() 키값들을 리턴해준다.