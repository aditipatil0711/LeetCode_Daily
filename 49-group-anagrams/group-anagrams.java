class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for(String str: strs){
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String signature = new String(charArray);

            if(!map.containsKey(signature)){
            map.put(signature,new ArrayList<>());
            }

            map.get(signature).add(str);
        }

        return new ArrayList<>(map.values());

}
}