# Segmentation

###### 2020.03.09

### I. 개념
- 프로그램은 의미 단위인 여러 개의 segment로 구성
  - 작게는 프로그램을 구성하는 함수 하나하나를세그먼트로 정의
  - 크게는 프로그램 전체를 하나의 세그먼트로 정의 가능
  - 일반적으로는 code, data, stack 부분이 하나씩의 세그먼트로 정의됨
  - 좀더 잘게 자르고 싶다면 다음들과 같이 자를 수 있음
    - main()
    - function
    - global varibles
    - stack
    - symbol table
    - arrays

- Logical Address는 <segment-number, offset> 두가지로 구성
- Segment table
  - each table entry has:
    - base - starting physical address of the segment
    - limit - length of the segment (의미 단위로 자르기에 길이가 동일하지 않아서 필요함)
- Segment table base register (STBR)
  - 물리적 메모리에서만의 segment table의 위치
- Segment table length register (STLR)
  - 프로그램이 사용하는 segment 수
  - 세그먼트 번호는 STLR보다 작아야한다.

### II. 특징
- Protection
  - 각 세그먼트 별로 protection bit가 있음
  - Each entry:
    - valid bit = 0 : illegal segment
    - Read/Write/Execution 권한 bit
- Sharing
  - shared segment
  - same segment number
  - segment는 의미단위이기 때문에 공유와 보안에 있어 paging보다 훨씬 효과적이다.
- Allocation
  - first fit / best fit
  - external fragmentation 발생
  - segment의 길이가 동일하지 않으므로 가변분할 방식에서와 동일한 문제점들이 발생
