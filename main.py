from typing import List


class Solution:

  def groupAnagrams(self, words: List[str]) -> List[List[str]]:
    obj = {}
    key = ''

    for word in words:
      # generate key for each word
      key = '/'.join(sorted([char for char in word]))
      # accumulate words in obj (dict)
      if key not in obj:
        obj[key] = [word]
      else:
        obj[key].append(word)

    return obj.values()


my = Solution()
n = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = my.groupAnagrams(n)
print("ans", ans)
