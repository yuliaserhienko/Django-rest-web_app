from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin

from .models import User
from .permissions import IsUserAccount, IsAdminOrUserAccount
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrUserAccount]

    @action(
        methods=['post'],
        detail=False,
        permission_classes=[IsUserAccount],
        url_path='confirm-email'
    )
    def confirm_email(self, request):
        """
        email confirmation
        """
        return Response()

    @action(
        methods=['get'],
        detail=False,
        permission_classes=[IsUserAccount],
        url_path='get-profile'
    )
    def profile(self, request):
        user = request.user
        self.check_object_permissions(self.request, user)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)


class LoginView(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)


class LogoutView(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class RegisterView(CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
