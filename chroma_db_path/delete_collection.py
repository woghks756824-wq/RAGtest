import chromadb

# ChromaDB 서버에 HTTP로 연결
# - localhost:8000 에 실행 중인 Chroma 서버 사용
chroma_client = chromadb.HttpClient(
    host="localhost",
    port=8000
)

# 삭제하려는 컬렉션 이름 지정
# - 기존에 생성했던 컬렉션 이름을 문자열로 지정
collection_name = "new_collection"

# ChromaDB에서 해당 컬렉션 삭제
# - 컬렉션에 저장된 모든 문서, 벡터, 메타데이터가 함께 삭제됨
chroma_client.delete_collection(
    name=collection_name
)

# 삭제 완료 메시지 출력
print(f"컬렉션 '{collection_name}' 삭제 완료")

pass