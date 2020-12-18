import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String in = sc.nextLine();
        String boom = sc.nextLine();

        StringBuffer sb = new StringBuffer();

        for (int i = 0; i < in.length(); i++) {
            String sub = in.substring(i, i+1);
            sb.append(sub);

            int sblen = sb.length();
            int blen = boom.length();
            if (sblen >= blen) {
                String sbsub = sb.substring(sblen - blen, sblen);
                if (sbsub.equals(boom)){
                    sb.delete(sblen - blen, sblen);
                }
            }
        }

        if (sb.toString().equals("")) System.out.println("FRULA");
        else System.out.println(sb.toString());

    }



}
