def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs :
            anagrams[''.join(sorted(word))].append(word) # sorted를 하면 조각조각 나뉘어 리스트로 반환되기에 join으로 붙이기
        
        return anagrams.values()
