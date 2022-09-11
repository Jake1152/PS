# nearest_common_anscestor_3584.md

# 문제이해
공통조상
호랑이,사자
호랑이 고양이
모두 고양이과

# 문제해결방법
- target list
- visited list
- stack방식
-  2D answer list
- 하나의 target을 찾으면 
    기존 list를 복제해서 answer list에 추가
    기존 list는 target list가 있는 동안 
- 가장가까운 공통조상 찾기 
    - 앞에서부터 찾으면서 공통되는 가장 마지막 케이스를 찾는다.
        - binsearch 쓸수도 있을 듯
        - 굳이 안써도 효율은 충분할듯