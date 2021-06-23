class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Set<String> book = new HashSet<>();

        Arrays.sort(phone_book);

        for (String phone : phone_book) {
            StringBuilder sb = new StringBuilder();
            for (char a : phone.toCharArray() ) {
                sb.append(a);
                System.out.println(sb.toString());
                if (book.contains(sb.toString())) return false;

            }
            book.add(sb.toString());
        }

        return answer;
    }
}