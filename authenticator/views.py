# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import jwt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authenticator.models import User
from django.http import Http404
from rest_framework.views import APIView
from authenticator.serializers import UserSerializer


class UserAuthView(APIView):
    """
    """
    def post(self, request, format=None):
        if not request.data:
            raise Http404

        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(username=username, password=password)
        except:
            return Response({'Error': "Invalid username/password"}, status="400")

        if user:
            payload = {
                'id': user.id,
                'email': user.email
            }

            jwt_token = jwt.encode(payload, 'SECRET')

            user.token = jwt_token
            user.save()

            return Response(data={'token': jwt_token})
        else:
            return Response(data={'error': 'Invalid Credentials'})


class UserView(APIView):
    """
    """
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
