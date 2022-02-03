  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anigma = collections.defaultdict(list) # keyError 방지


        for word in strs :
            anigma[''.join(sorted(word))].append(word) # sorted하면 조각조각으로 반환 

        return anigma.values()
