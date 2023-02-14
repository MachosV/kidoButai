from io import BytesIO
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import generics
from PIL import Image as PILImage
from ..serializers import ImageSerializer

class ImageUploader(generics.CreateAPIView):
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
      image = request.data['image']
      print(type(image))
      image = PILImage.open(image)
      max_size = (400, 400)
      if image.height > 800 or image.width > 800:
        image.thumbnail(max_size)
      image_io = BytesIO()
      image.save(image_io, format='JPEG')
      image_io.seek(0)
      #print(image_io.read())
      request.data['image'] = image_io.read()
      serializer = self.get_serializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
      return Response(serializer.errors, status=400)


