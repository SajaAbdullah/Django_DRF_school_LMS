from rest_framework import viewsets
from rest_framework.response import Response

from .utils import get_collection_handle, get_db_handle


class MongoTeacherViewSet(viewsets.ViewSet):

    # setup mongoDB connection using PyMongo
    MONGO_HOST = "127.0.0.1"
    MONGO_PORT = "27017"
    MONGO_DB = "teacher_training"
    MONGO_COLLECTION = "training_material"
    MONGO_USER = "saja"
    MONGO_PASS = "123456"
    connection_string = "mongodb://{}:{}@{}:{}/{}?authSource=teacher_training".format(
        MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB
    )
    db_handle, mongo_client = get_db_handle(MONGO_DB, connection_string)
    collection_handle = get_collection_handle(db_handle, MONGO_COLLECTION)

    def create(self, request):
        """Create method to insert data into mongo DB"""
        self.collection_handle.insert_one(
            {
                "uuid": str(request.data.get("uuid")),
                "index": str(request.data.get("index")),
                "title": str(request.data.get("title")),
            }
        )
        return Response(status=201)

    def list(self, request):
        """list all document in teacher_training collection"""
        cur = self.collection_handle.find({}, {"_id": 0})
        training_data = list(cur)

        return Response({"training data": training_data}, status=200)

    def retrieve(self, request, pk=None):
        """fetch single document"""
        uuid = pk
        training_data = self.collection_handle.find_one({"uuid": str(uuid)}, {"_id": 0})
        return Response(training_data, status=200)

    def update(self, request, pk=None):
        """update single document"""
        uuid = pk
        self.collection_handle.update_one(
            {"uuid": str(uuid)}, {"$set": {"title": str(request.data.get("title"))}}
        )
        return Response(status=200)

    def destroy(self, request, pk=None):
        """method to delete single document"""
        uuid = pk
        self.collection_handle.delete_one({"uuid": str(uuid)})
        return Response(status=200)
