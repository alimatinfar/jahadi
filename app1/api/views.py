from rest_framework import generics
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.filters import SearchFilter, OrderingFilter

from .permissions import OwnerCanManageReadOnly
from app1.models import Profile, Hamkari, User, Farakhan, Profile_present, Profile_ready, Hamkari_code
from rest_framework.authentication import TokenAuthentication
from .serializers import ProfileSerializer, HamkariSerializer, Hamkari_codeserializer, LoginSerilizer, Userserializer, \
    Farakhanserializer, Profile_presentserializer, Profile_readyserializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import exceptions, status

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


class UserCreateAPIView(generics.GenericAPIView):

    def post(self, request):
        user = User()
        try:
            user.username = request.data.get("username")
        except:
            raise exceptions.ValidationError("username is required")

        try:
            user.set_password(request.data.get("password"))
        except:
            raise exceptions.ValidationError("password is required")
        user.is_active = True
        user.save()
        return Response({'username':user.username, 'password': user.password, 'id': user.id},status=status.HTTP_201_CREATED)


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


class FarakhanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Farakhan.objects.all()
    serializer_class = Farakhanserializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filterset_fields = ('owner__username', 'content', 'title')
    # search_fields = ('owner__username', 'content', 'title')
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class FarakhanUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farakhan.objects.all()

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = Farakhanserializer
    lookup_field = 'id'


class Profile_readyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile_ready.objects.all()
    serializer_class = Profile_readyserializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filterset_fields = ('owner__username', 'content', 'title')
    # search_fields = ('owner__username', 'content', 'title')
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Profile_readyUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile_ready.objects.all()

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = Profile_readyserializer
    lookup_field = 'id'


class Profile_presentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile_present.objects.all()
    serializer_class = Profile_presentserializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filterset_fields = ('owner__username', 'content', 'title')
    # search_fields = ('owner__username', 'content', 'title')
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Profile_presentUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile_present.objects.all()

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = Profile_presentserializer
    lookup_field = 'id'


class Hamkari_codeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hamkari_code.objects.all()
    serializer_class = Hamkari_codeserializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filterset_fields = ('owner__username', 'content', 'title')
    # search_fields = ('owner__username', 'content', 'title')
    lookup_field = 'id'
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Hamkari_codeUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hamkari_code.objects.all()

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = Hamkari_codeserializer
    lookup_field = 'id'
