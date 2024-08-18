from django.urls import path
from .views import edit_image_dalle2, change_image_dalle2, gen_image_dalle3

urlpatterns = [
    path('images/dalle-2/edit/', edit_image_dalle2, name='edit_image_dalle2'),
    path('images/dalle-2/alter', change_image_dalle2, name='edit_image_dalle2'),
    path('images/dalle-3/generate', gen_image_dalle3, name='gen_image_dalle3'),
]
