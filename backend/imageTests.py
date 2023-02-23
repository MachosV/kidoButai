from io import BytesIO
from PIL import Image as PILImage


image = PILImage.open(r"ironMaiden.jpg")

max_size = (400, 400)
if image.height > 400 or image.width > 400:
    image.thumbnail(max_size)
    image.save("thumbnail.jpg", format='JPEG')