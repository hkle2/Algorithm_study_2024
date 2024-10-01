class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            str_dict[sorted_string].append(string)
        return str_dict.values()