from pypdf import PdfReader

def load_pdf_text(pdf_path: str) -> str:
    # """
    # PDF 파일 경로를 받아서
    # PDF 전체 텍스트를 하나의 문자열로 반환하는 함수
    # """

    # PDF 파일 열기
    # - pdf_path에 있는 PDF 파일을 읽기 전용으로 로드
    reader = PdfReader(pdf_path)

    # PDF 전체 텍스트를 누적할 문자열
    full_text = ""

    # PDF의 모든 페이지를 순회
    for page in reader.pages:
        # 각 페이지에서 텍스트 추출
        text = page.extract_text()

        # 페이지에 텍스트가 있을 경우만 추가
        if text:
            full_text += text + "\n"

    # 모든 페이지의 텍스트를 하나로 합쳐 반환
    return full_text
