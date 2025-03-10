class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        h번 이상 인용된 논문의 수가 h편 이상이어야하며

        min(인용된 논문의 수, 인용 수)
        h가 최대가 되는 값이 h-index

        # way 0
        1. asc sort
        2. linear search
          - min(논문 인용수, 인용된 논문의 수)이 값이 최대가 되는 값
          - 맨 왼쪽부터 시작
          - paper 수와 인용 수
          - 페이퍼 수: last_idx - idx
          - 현재 인용: papers[idx]
          - 0일때?
          
        # way 1
        1. sort
        2. bin-search
        3. return h-index
        # 최소 h 회 이상 인용된 최소 h 편의 논문을 출판했다는 h 의 최대값
        '''
        # for in range()
        sorted_citations = sorted(citations)
        paper_count = len(sorted_citations)
        h_index = -1
        for idx, citation in enumerate(sorted_citations):
            citation_paper_count = paper_count - idx
            # citation_paper_count을 넣지 않아서 문제가 되었었음
            cur_h_index = min(citation, citation_paper_count)
            if cur_h_index < h_index:
                break
            h_index = cur_h_index
        return h_index
