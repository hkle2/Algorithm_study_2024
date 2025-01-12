class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            d[key].append(word)
        return list(d.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            str_dict[sorted_s].append(s)
        return str_dict.values()