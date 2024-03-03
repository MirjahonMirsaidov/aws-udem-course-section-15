from rest_framework.generics import CreateAPIView

from userprofile.serializers.file_upload import FileUploadSerializer


class FileUploadGenericView(CreateAPIView):
    serializer_class = FileUploadSerializer
