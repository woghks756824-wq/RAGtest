def split_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
):
    """
    긴 텍스트를 일정 길이의 조각(chunk)으로 나누는 함수

    - chunk_size: 한 조각의 최대 문자 수
    - overlap: 이전 조각과 겹치는 문자 수 (문맥 유지를 위해)
    """

    # 분할된 텍스트 조각들을 저장할 리스트
    chunks = []

    # 현재 자르기 시작할 위치 인덱스
    start = 0

    # 텍스트 끝에 도달할 때까지 반복
    while start < len(text):
        # 현재 조각의 끝 위치 계산
        end = start + chunk_size

        # 텍스트를 start ~ end 범위로 자르기
        chunk = text[start:end]

        # 잘라낸 조각을 리스트에 추가
        chunks.append(chunk)

        # 다음 조각 시작 위치 설정
        # overlap 만큼 이전 내용과 겹치게 설정
        start = end - overlap

    # 모든 조각 반환
    return chunks