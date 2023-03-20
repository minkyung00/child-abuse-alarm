from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .serializers import CenterSerializer, CenterUserSerializer
from .models import Center, User

class CenterView(APIView):
    def get(self, request):
        centers = Center.objects.all()
        keyword = request.GET.get('keyword', '')

        if keyword:
            centers = centers.filter(name__icontains=keyword)

        serializer = CenterSerializer(centers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CenterCodeView(APIView):
    def get_center(self, center_id):
        center = get_object_or_404(Center, id=center_id)
        return center
    
    def post(self, request, center_id):
        center = self.get_center(center_id)

        if center is False:
            return Response({"error": "존재하지 않는 어린이집입니다."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username = request.user).filter(center = center.name).count():
            return Response({"error": "이미 등록된 어린이집입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {}
        data["username"] = request.user.username
        data["center_id"] = center_id
        serializer = CenterUserSerializer(data=data)

        code = request.data["code"]
        if code == center.code:
            request.user.center = center.name
            request.user.save()

            if serializer.is_valid():
                serializer.save()
                data['center_name'] = center.name
                return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "유효하지 않은 코드입니다."}, status=status.HTTP_401_UNAUTHORIZED)