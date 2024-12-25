from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import re

class RegisterView(APIView):
    def post(self, request):
        # الحصول على البيانات من الطلب
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # التحقق من وجود الحقول المطلوبة
        if not username or not email or not password:
            return Response({"error": "Username, email, and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # التحقق من وجود المستخدم مسبقًا
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        # التحقق من صحة البريد الإلكتروني باستخدام تعبير نمطي
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return Response({"error": "Invalid email address"}, status=status.HTTP_400_BAD_REQUEST)

        # إنشاء مستخدم جديد
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # تشفير كلمة المرور
        )
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
