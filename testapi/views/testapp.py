from rest_framework import generics, serializers
from rest_framework.response import Response

from testapp.models.members import Member

class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'email', 'created_at', 'updated_at')

class MemberListView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        return Response(serializer.data)




