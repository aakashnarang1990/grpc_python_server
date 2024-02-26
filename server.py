from concurrent import futures
import grpc

from protos import clothing_store_pb2_grpc
from protos import clothing_store_pb2



class RemoteCallServicer(clothing_store_pb2_grpc.ClothingStoreServicer):
    """
    RPC Server Class
    """
    def GetArticleByBarcode(self, request, context):
        print("serving")
        article = clothing_store_pb2.ArticleSearchResponse(
            item_type="t-shirt", 
            size = "m", 
            colour = "blue", 
            stock = 5, 
            price = 1000, 
            offers=[
                {"discount_percent": 10.0},
                {"discount_percent": 5.0}
                ]
                )
        return article


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    clothing_store_pb2_grpc.add_ClothingStoreServicer_to_server(
        RemoteCallServicer(), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()