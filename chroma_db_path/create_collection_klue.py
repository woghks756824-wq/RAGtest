import chromadb
from chromadb.utils import embedding_functions

# SentenceTransformer 기반 임베딩 함수 생성
# - Hugging Face에 있는 "Huffon/sentence-klue-roberta-base" 모델을 사용
# - 한국어 문장 임베딩에 최적화된 모델
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="Huffon/sentence-klue-roberta-base"
)

# ChromaDB 서버에 HTTP로 연결
# - localhost:8000 에 실행 중인 Chroma 서버 사용
chroma_client = chromadb.HttpClient(
    host="localhost",
    port=8000
)

# 컬렉션 가져오기 또는 생성
# - "korean_pdf_collection" 이 이미 있으면 그대로 사용
# - 없으면 새로 생성
# - 이 컬렉션은 klue-roberta 임베딩 함수로 고정됨
collection = chroma_client.get_or_create_collection(
    name="korean_pdf_collection",
    embedding_function=embedding_function
)

# 컬렉션 생성 완료 메시지 출력
print("klue-roberta 전용 컬렉션 생성")

# 현재 ChromaDB에 존재하는 모든 컬렉션 목록 출력
print("컬렉션 목록:", chroma_client.list_collections())
