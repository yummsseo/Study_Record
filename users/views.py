from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from .serializers import UserCreationSerializer

@ensure_csrf_cookie
def login_html(request):
    return render(request, 'login.html')

class SignupView(views.APIView):
    permission_classes = [AllowAny]
    # 회원가입은 기존 설정을 유지합니다
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch') # CSRF 검사를 이 뷰에서만 제외
class LoginView(views.APIView):
    permission_classes = [AllowAny]
    authentication_classes = [] # 세션 인증의 CSRF 강제를 피하기 위해 비워둡니다

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # 세션 로그인 수행
            return Response({'message': f'{user.username}님 환영합니다!'}, status=status.HTTP_200_OK)
        return Response({'error': '아이디 또는 비밀번호가 틀렸습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        logout(request)
        return Response({'message': '로그아웃 성공'}, status=status.HTTP_200_OK)