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


import json
from django.core import serializers
from app1.models import Profile, Hamkari, User, Farakhan, Profile_present, Profile_ready, Hamkari_code
from rest_framework.authentication import TokenAuthentication
from .serializers import ProfileSerializer, HamkariSerializer, Hamkari_codeserializer, LoginSerilizer, Userserializer, \
    Farakhanserializer, Profile_presentserializer, Profile_readyserializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import exceptions, status
from django.shortcuts import get_object_or_404

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


class ProfileCreateAPIView(generics.GenericAPIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

        #
        # user_serialized = serializers.serialize('json', user)
        # user_json = json.loads(user_serialized)
        # user_json = user_json[0]

        try:
            email = request.data.get("email")
        except:
            raise exceptions.ValidationError("email is required")

        try:
            first_name = request.data.get("first_name")
        except:
            raise exceptions.ValidationError("first_name is required")

        try:
            last_name = request.data.get("last_name")
        except:
            raise exceptions.ValidationError("last_name is required")


        try:
            national_code = request.data.get("national_code")
        except:
            raise exceptions.ValidationError("national_code is required")

        try:
            date_birth = request.data.get("date_birth")
        except:
            raise exceptions.ValidationError("date_birth is required")

        try:
            gender = request.data.get("gender")
        except:
            raise exceptions.ValidationError("gender is required")

        try:
            marital = request.data.get("marital")
        except:
            raise exceptions.ValidationError("marital is required")

        try:
            address = request.data.get("address")
        except:
            raise exceptions.ValidationError("address is required")


        try:
            mobile = request.data.get("mobile")
        except:
            raise exceptions.ValidationError("mobile is required")


        try:
            picture = request.data.get("picture")
        except:
            pass

        try:
            father_name = request.data.get("father_name")
        except:
            raise exceptions.ValidationError("father_name is required")


        profile = Profile.objects.create(user=user, email= email, first_name= first_name,
                                         last_name= last_name, national_code= national_code, date_birth= date_birth,
                                         gender = gender, marital = marital,  mobile = mobile, father_name = father_name)


        profile.save()

        return Response({'username':user.username, 'password' : user.password, 'first_name' : first_name}, status=status.HTTP_201_CREATED)

        #
        # profile_serialized = serializers.serialize('json', profile)
        # profile_json = json.loads(profile_serialized)
        # profile_json = profile_json[0]
        #
        # user_json.update(profile_json)



class UserEditAPIView(generics.GenericAPIView):

    def put(self, request, id=None):
        if id:
            user = get_object_or_404(User, id=id)
            active = user.is_active
            staff = user.is_staff
            superuser = user.is_superuser
            print(user.is_superuser)
            serialize = Userserializer(user, data=request.data)
            if serialize.is_valid():
                try:
                    user.username = request.data.get("username")
                except:
                    raise exceptions.ValidationError("username is required")

                try:
                    user.set_password(request.data.get("password"))
                except:
                    raise exceptions.ValidationError("password is required")

                user.is_active = active
                user.is_staff = staff
                user.is_superuser = superuser
                user.save()
                return Response(serialize.data, status=status.HTTP_200_OK)
            else:
                return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            raise exceptions.ValidationError("id is null")


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
