from rest_framework import serializers, exceptions
from app1.models import Profile, Hamkari, Farakhan, Profile_present, Profile_ready, Hamkari_code
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class LoginSerilizer(serializers.Serializer):
    username = serializers.CharField()

    password = serializers.CharField()

    def validate(self, data):

        username = data.get("username", "")

        password = data.get("password", "")

        if username and password:

            user = authenticate(username=username, password=password)

            if user:

                if user.is_active:

                    data["user"] = user

                else:

                    msg = "کاربر غیرفعال می باشد"

                    raise exceptions.ValidationError(msg)

            else:

                msg = "نام کاربری یا گذرواژه اشتباه است"

                raise exceptions.ValidationError(msg)

        else:

            msg = "نام کاربری و کلمه عبور اجباری می باشد"

            raise exceptions.ValidationError(msg)

        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class HamkariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamkari
        fields = "__all__"


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    validate_password = make_password#حل مشکل نشناختن الگوریتم رمز عبور !!!!!!!!!!!!!!


class Farakhanserializer(serializers.ModelSerializer):
    class Meta:
        model = Farakhan
        fields = "__all__"


class Profile_readyserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_ready
        fields = "__all__"


class Profile_presentserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_present
        fields = "__all__"


class Hamkari_codeserializer(serializers.ModelSerializer):
    class Meta:
        model = Hamkari_code
        fields = "__all__"
