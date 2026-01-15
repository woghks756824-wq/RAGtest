import chromadb
from chromadb.utils import embedding_functions
import requests

# SentenceTransformer 임베딩 함수 설정
# - PDF를 벡터화할 때 사용한 것과 동일한 klue-roberta 모델
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="Huffon/sentence-klue-roberta-base"
)

# 실행 중인 ChromaDB 서버에 연결
chroma_client = chromadb.HttpClient(
    host="localhost",
    port=8000
)

# PDF가 저장된 기존 컬렉션 불러오기
# - 반드시 같은 embedding_function을 지정해야 함
collection = chroma_client.get_collection(
    name="korean_pdf_collection",
    embedding_function=embedding_function
)

# 사용자 질문 정의
query = "전단 설계 기준은 무엇인가?"

# ChromaDB에서 질문과 가장 유사한 문단 검색
# - n_results=3 → 상위 3개 문단 반환
results = collection.query(
    query_texts=[query],
    n_results=3
)

# 검색된 문단 텍스트만 추출
docs = results["documents"][0]

# 여러 문단을 하나의 컨텍스트 문자열로 결합
context = "\n\n".join(docs)

# LLM(Ollama)에 전달할 프롬프트 구성
# - "문서 기반으로만 답변하라"는 RAG 핵심 지시 포함
prompt = f"""
너는 건설 구조 기준 문서를 해석하는 전문가다.

아래 문서 내용만 근거로 질문에 답하라.
문서에 없는 내용은 추측하지 마라.

[문서]
{context}

[질문]
{query}
"""

# Ollama 로컬 서버에 요청 전송
# - http://localhost:11434 는 Ollama 기본 주소
# - model: llama3 (Modelfile로 만든 모델 이름)
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
)

# LLM이 생성한 최종 답변 출력
print("답변:")
print(response.json()["response"])