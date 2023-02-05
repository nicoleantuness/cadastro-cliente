from django.shortcuts import get_object_or_404
from .models import Contacts, ContactsList
from accounts.models import Account
from .serializer import ContactSerializer, ContactsListSerializer
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics

class ContactAccountView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contacts.objects.filter(account_id=self.kwargs["account_id"])

    def perform_create(self, serializer):
        account_id = self.kwargs["account_id"]
        
        account_obj = get_object_or_404(Account, id=account_id)
    
        serializer.save(account=account_obj)
    
    # def post(self, request:Request, account_id) -> Response:
    #     contact_obj = get_object_or_404(Contacts, pk=account_id)
        
    #     self.check_object_permissions(request, account_id)
    #     serializer = ContactSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(contact = contact_obj, account=request.account)

    #     return Response(serializer.data, status.HTTP_201_CREATED)

class GetOneContactView(APIView):
    def get(self, request: Request, contact_id) -> Response:
        contact = Contacts.objects.get(id = contact_id)

        serializer = ContactSerializer(contact)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, contact_id) -> Response:

            contact = Contacts.objects.get(id = contact_id)

            contact.delete()

            return Response(status=204)
class ContactsListView(APIView):

    def post(self, request: Request, contact_id) -> Response:
        # ipdb.set_trace()
        contact_obj = get_object_or_404(Contacts, pk=contact_id)
        
        self.check_object_permissions(request, contact_obj)
        serializer = ContactsListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(contact = contact_obj, account=request.account)

        return Response(serializer.data, status.HTTP_201_CREATED)