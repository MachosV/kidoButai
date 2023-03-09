from io import BytesIO
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import generics
from PIL import Image as PILImage
from ..serializers import ImageSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import hashlib
import uuid


class ImageUploader(generics.CreateAPIView):
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
      
        image_file = request.data.get('image')
        image = PILImage.open(image_file)

        if not image.format.lower() in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']:
          return Response({'error': 'Invalid image format'}, status=400)


        max_size = (200, 200)
        if image.height > 200 or image.width > 200:
          image.thumbnail(max_size)
        
        image_io = BytesIO()
        newImageFilename = str(hashlib.md5(image.filename.encode('utf-8')).hexdigest())[0:4]+str(uuid.uuid4())[-8:-1]
        image.save(image_io, filename = newImageFilename, format = image.format.lower())
        image_io.seek(0)
        
        if image_file:
            file_name = default_storage.save("images/"+newImageFilename+"."+image.format.lower(), ContentFile(image_io.read()))
            file_url = default_storage.url(file_name)
            image_io.close()
            print(file_url)
            return Response({'file_url': file_url}, status=201)
        else:
            image_io.close()
            return Response({'error': 'No image file provided.'}, status=400)


