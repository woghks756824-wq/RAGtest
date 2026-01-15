import chromadb
from chromadb.utils import embedding_functions

# Sentence-Transformer 기반 임베딩 함수 생성
# - 한국어 문서에 적합한 klue-roberta 모델 사용
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="Huffon/sentence-klue-roberta-base"
)

# 실행 중인 ChromaDB 서버에 HTTP로 연결
# - localhost:8000 에 떠 있는 Chroma 서버 사용
client = chromadb.HttpClient(
    host="localhost",
    port=8000
)

# 기존에 생성되어 있는 컬렉션 가져오기
# - PDF를 벡터화해 저장해둔 컬렉션
# - 반드시 같은 embedding_function을 사용해야 함
collection = client.get_collection(
    name="pdf_collection_klue",
    embedding_function=embedding_function
)

# 컬렉션에 질의(Query) 수행
# - query_texts: 자연어 질문 (Chroma가 자동으로 임베딩)
# - n_results: 가장 유사한 문서 몇 개를 반환할지
results = collection.query(
    query_texts=["이 문서의 핵심 내용은 무엇인가?"],
    n_results=3
)

# 검색된 결과 출력
# - results["documents"][0] 에 실제 텍스트 문단들이 들어 있음
for i, doc in enumerate(results["documents"][0]):
    print(f"\n--- RESULT {i+1} ---")
    print(doc)
