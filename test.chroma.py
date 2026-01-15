import chromadb
import uuid
from chromadb.utils import embedding_functions

# ===============================
# 1klue-roberta 임베딩 함수
# ===============================
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="Huffon/sentence-klue-roberta-base"
)

# ===============================
# Chroma 서버 연결
# ===============================
chroma_client = chromadb.HttpClient(
    host="localhost",
    port=8000
)

# ===============================
# 컬렉션 생성
# ===============================
collection = chroma_client.get_or_create_collection(
    name="new_collection_klue",   # ← 여기 중요
    embedding_function=embedding_function
)

print("COLLECTIONS:", chroma_client.list_collections())

# ===============================
# 문서 추가
# ===============================
documents = [
    "파인애플은 열대 과일이다",
    "오렌지는 비타민 C가 풍부하다",
    "사과는 하루 한 개면 의사가 필요 없다",
    "내 이름은 JeongTae Park이다"
]

ids = [str(uuid.uuid4()) for _ in documents]

metadatas = [
    {"index": i, "version": 1.0} for i in range(len(documents))
]

collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print("\nAFTER ADD:")
print(collection.peek())
print("COUNT:", collection.count())

# ===============================
# 검색 테스트 (query_texts만 사용)
# ===============================
print("\n--- QUERY 1: 열대 과일 ---")
results = collection.query(
    query_texts=["열대 과일에 대한 문서"],
    n_results=1
)
print(results)

print("\n--- QUERY 2: 이름 ---")
results = collection.query(
    query_texts=["내 이름은 무엇인가?"],
    n_results=1
)
print(results)

print("\n--- QUERY 3: 사과 ---")
results = collection.query(
    query_texts=["사과에 대해 설명한 문서"],
    n_results=1
)
print(results)