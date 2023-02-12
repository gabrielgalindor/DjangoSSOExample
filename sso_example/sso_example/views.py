from rest_framework import generics
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from .serializers import UserSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        credentials = Credentials.from_authorized_user_info(info=request.data)
        service = build('oauth2', 'v2', credentials=credentials)
        user_info = service.userinfo().get().execute()
        # Use the user information to create a Django user and save it to the database
        # ...
        # Return a response with the user's token
        return Response({"token": user.auth_token.key})