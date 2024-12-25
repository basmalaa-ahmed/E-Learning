from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

class LoginView(APIView):
    def post(self, request):
        # التحقق من وجود اسم المستخدم وكلمة المرور في البيانات المرسلة
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ValidationError("اسم المستخدم وكلمة المرور مطلوبان")

        # التحقق من بيانات المستخدم
        user = authenticate(username=username, password=password)

        if user is not None:
            # إنشاء أو استرجاع التوكن
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "اسم المستخدم أو كلمة المرور غير صحيحة"}, status=status.HTTP_401_UNAUTHORIZED)
