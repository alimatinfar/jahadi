from rest_framework import generics
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.filters import SearchFilter, OrderingFilter

from .permissions import OwnerCanManageReadOnly
from app1.models import Profile, Hamkari, User
from rest_framework.authentication import TokenAuthentication
from .serializers import ProfileSerializer, HamkariSerializer, LoginSerilizer, Userserializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@method_decorator(csrf_exempt, name='dispatch')
class Login222(generics.GenericAPIView):
    serializer_class = LoginSerilizer

    def post(self, request):
        serializer = LoginSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "userid": user.id, "user": Userserializer(user, many=False).data},
                        status=200)


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filterset_fields = ('owner__username', 'content', 'title')
    # search_fields = ('owner__username', 'content', 'title')
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ProfileUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = ProfileSerializer
    lookup_field = 'id'


class HamkariListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hamkari.objects.all()
    serializer_class = HamkariSerializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filterset_fields = ('owner__username', 'content', 'title')
    # search_fields = ('owner__username', 'content', 'title')
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class HamkariUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hamkari.objects.all()

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = HamkariSerializer
    lookup_field = 'id'


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filterset_fields = ('owner__username', 'content', 'title')
    # search_fields = ('owner__username', 'content', 'title')
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class UserUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = Userserializer
    lookup_field = 'id'