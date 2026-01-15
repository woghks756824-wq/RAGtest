import chromadb
from chromadb.utils import embedding_functions

# SentenceTransformer 기반 임베딩 함수 생성
# - 한국어 문서에 적합한 klue-roberta 모델 사용
# - PDF를 저장할 때 사용한 임베딩 모델과 반드시 같아야 함
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="Huffon/sentence-klue-roberta-base"
)

# 실행 중인 ChromaDB 서버에 HTTP로 연결
# - Docker 또는 로컬에서 실행 중인 Chroma 서버 (localhost:8000)
chroma_client = chromadb.HttpClient(
    host="localhost",
    port=8000
)

# 기존에 생성된 컬렉션 가져오기
# - PDF 문서들을 벡터화해 저장해 둔 컬렉션
# - embedding_function을 동일하게 지정해야 충돌 에러가 나지 않음
collection = chroma_client.get_collection(
    name="korean_pdf_collection",
    embedding_function=embedding_function
)

# 컬렉션에 질의(Query) 수행
# - query_texts: 자연어 질문 (Chroma가 내부적으로 임베딩 생성)
# - n_results: 가장 유사한 문서(문단) 몇 개를 반환할지
results = collection.query(
    query_texts=["전단 설계 기준은 무엇인가?"],
    n_results=3
)

# 검색 결과 출력
# - results["documents"][0] 안에 실제로 매칭된 텍스트 문단들이 들어 있음
print("검색 결과:")
for doc in results["documents"][0]:
    print("-" * 30)
    print(doc)
