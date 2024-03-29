from rest_framework import serializers, generics, mixins, views
from rest_framework.response import Response
from core.models import Visitors, VisitorGroup, VisitorsLocation
from api.permissions import *
from api.serializer import *


class VisitorsGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitorGroup
        fields = ('group_name', 'black_listed', 'uuid', 'created', 'modified', 'modified_by', 'created_by', 'params')
        lookup_field = 'uuid'
        filter_fields = ('group_name', 'black_listed', 'uuid',)


class VisitorsGroupDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                          generics.GenericAPIView, mixins.CreateModelMixin):

    model = VisitorGroup
    serializer_class = VisitorsGroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
    filter_fields = ('group_name', 'black_listed', 'uuid',)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitorsGroupList(generics.ListAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,):
    model = VisitorGroup
    serializer_class = VisitorsGroupSerializer
    filter_fields = ('group_name', 'black_listed', 'uuid',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VisitorsLocationSerializer(serializers.ModelSerializer):
    visitor_id = UUIDRelatedField(many=False)

    class Meta:
        model = VisitorsLocation
        fields = ('visitor_id', 'residential_country', 'residential_state', 'residential_state', 'residential_lga',
                  'contact_address', 'uuid', 'created', 'modified', 'modified_by', 'created_by')
        lookup_field = 'uuid'
        filter_fields = ('visitor_id',)


class VisitorSerializer(serializers.ModelSerializer):
    group_type = UUIDRelatedField()

    class Meta:
        model = Visitors
        fields = ('first_name', 'last_name', 'visitors_email', 'visitors_phone', 'date_of_birth', 'group_type',
                  'state_of_origin', 'lga_of_origin', 'image', 'occupation', 'company_name', 'company_address',
                  'fingerprint', 'scanned_signature', 'visitors_pass_code', 'nationality', 'uuid', 'created',
                  'modified', 'modified_by', 'created_by', 'gender')
        lookup_field = 'uuid',


class VisitorNestedSerializer(serializers.ModelSerializer):
    current_location = VisitorsLocationSerializer(many=False)
    group_type = VisitorsGroupSerializer(many=False)
    class Meta:
        model = Visitors
        fields = ('first_name', 'last_name', 'visitors_email', 'visitors_phone', 'date_of_birth', 'group_type',
                  'state_of_origin', 'lga_of_origin', 'image', 'occupation', 'company_name', 'company_address',
                  'fingerprint', 'scanned_signature', 'visitors_pass_code', 'nationality', 'uuid', 'current_location',
                  'created', 'modified', 'modified_by', 'created_by', 'gender')
        lookup_field = 'uuid'


class VisitorsLocationList(generics.ListAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,):
    model = VisitorsLocation
    serializer_class = VisitorsLocationSerializer
    filter_fields = ('visitor_id',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VisitorsLocationDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                             generics.GenericAPIView, mixins.CreateModelMixin):

    model = VisitorsLocation
    serializer_class = VisitorsLocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'
    filter_fields = ('visitor_id',)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitorsList(generics.ListAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,):

    model = Visitors
    serializer_class = VisitorSerializer
    filter_fields = ('visitors_email', 'visitors_phone', 'visitors_pass_code', 'fingerprint', 'date_of_birth',
                     'created', 'modified', 'modified_by', 'created_by', 'group_type', 'gender')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VisitorsNestedList(generics.ListAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,):

    model = Visitors
    serializer_class = VisitorNestedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_fields = ('visitors_email', 'visitors_phone', 'visitors_pass_code', 'group_type', 'fingerprint',
                     'date_of_birth', 'created', 'modified', 'modified_by', 'created_by', 'gender')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class VisitorNestedDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                          generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Visitors.objects.all()
    serializer_class = VisitorNestedSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Visitors.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitorOwnDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Visitors.objects.all()
    serializer_class = VisitorSerializer
    lookup_field = 'visitor_pass_code'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthenticateVisitor(views.APIView):

    def post(self, request):
        return Response({'error_message': '', 'message': 'message was queued to be sent'})