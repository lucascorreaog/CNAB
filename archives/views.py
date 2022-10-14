import os

from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

from .models import File
from .serializers import FileSerializer, FileUploaderSerializer

class ArchiveView(APIView):
    def post(self, request: Request)-> Response:
        with open("CNAB.txt", "r") as f:
            line_read = f.readlines()
        for index in line_read:
            transaction_type = index[0]
            dateY = index[1:5]
            dateM = index[5:7]
            dateD = index[7:9]
            amount = int(index[9:19]) / 100
            cpf = index[19:30]
            card_number = index[30:42]
            time = index[42:48]
            store_owner = index[48:62]
            store = index[62:81]
            
            keys = {
                "transaction_type": transaction_type,
                "date": dateD + "/" + dateM + "/" + dateY,
                "amount": amount,
                "cpf": cpf,
                "card_number": card_number,
                "time": time,
                "store_owner": store_owner,
                "store": store,
            }
            
            serializer = FileSerializer(data=keys)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
        infos_list = File.objects.all()
        serializer = FileSerializer(data=infos_list, many=True)
        os.remove("CNAB.txt")
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def get(self, request: Request)-> Response:
        infos_list = File.objects.all()
        serializer = FileSerializer(data=infos_list, many=True)
        return Response(serializer.data)

class UploadedFile(generics.CreateAPIView):
    serializer_class = FileUploaderSerializer
