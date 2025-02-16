class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        h번 이상 인용된 논문의 수가 h편 이상이어야하며
        h가 최대가 되는 값이 h-index
        1. sort
        2. bin-search
        3. return h-index

        # 최소 h 회 이상 인용된 최소 h 편의 논문을 출판했다는 h 의 최대값
        '''
        sorted_citations = sorted(citations)
        print(f"{sorted_citations=}")
        # for in range()
        citations_set = set(citations)
        citations_list = [ citation for citation in citations_set ]
        paper_count = len(citations_list)
        begin = 0
        end = paper_count - 1
        while begin <= end:
            mid = (begin + end) // 2
            h_index_papers_count = paper_count - mid
            citation = citations_list[mid]
            if citation > h_index_papers_count:
                begin = mid + 1
            elif citation < h_index_papers_count:
                end = mid - 1
            else:
                break
        h_index = mid
        print(f"{h_index=}")
        print(f"{citations_list=}")
        return  mid + 1 if citations_list[h_index] else citations_list[h_index]

