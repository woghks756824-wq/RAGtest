import chromadb
from chromadb.utils import embedding_functions
from pdf_loader import load_pdf_text
import uuid

# klue-roberta 임베딩 함수
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="Huffon/sentence-klue-roberta-base"
)

# Chroma 서버 연결
chroma_client = chromadb.HttpClient(
    host="localhost",
    port=8000
)

# klue-roberta 전용 컬렉션 가져오기
collection = chroma_client.get_collection(
    name="korean_pdf_collection",
    embedding_function=embedding_function
)

# PDF 로드
pdf_path = "kds142062.pdf"   # 실제 PDF 경로
text = load_pdf_text(pdf_path)

# 문단 단위 분리
chunks = [t.strip() for t in text.split("\n\n") if len(t.strip()) > 30]
print(f"총 문단 수: {len(chunks)}")

# Chroma에 저장
collection.add(
    documents=chunks,
    ids=[str(uuid.uuid4()) for _ in range(len(chunks))]
)

print("PDF 벡터화 완료")
print("총 저장 개수:", collection.count())