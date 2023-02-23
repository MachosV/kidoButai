from io import BytesIO
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import generics
from PIL import Image as PILImage
from ..serializers import ImageSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class ImageUploader(generics.CreateAPIView):
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
      # image = request.data['image']
      # image = PILImage.open(image)
      # max_size = (200, 200)
      # if image.height > 200 or image.width > 200:
      #   image.thumbnail(max_size)
      # image_io = BytesIO()
      # image.save(image_io, format='JPEG')
      # image_io.seek(0)

      # uploaded_file = InMemoryUploadedFile(
      #   file=image_io,
      #   field_name='image',
      #   name='image.png',
      #   content_type='image/png',
      #   size=len(image_io.getvalue()),
      #   charset=None,
      # )
        image_file = request.data.get('image')
        image = PILImage.open(image_file)
        max_size = (200, 200)
        if image.height > 200 or image.width > 200:
          image.thumbnail(max_size)
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        
        if image_file:
            file_name = default_storage.save("images/"+image_file.name, ContentFile(image_io.read()))
            file_url = default_storage.url(file_name)
            image_io.close()
            return Response({'file_name': file_name, 'file_url': file_url}, status=201)
        else:
            image_io.close()
            return Response({'error': 'No image file provided.'}, status=400)


