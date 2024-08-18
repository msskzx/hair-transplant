from openai import OpenAI
import os
from django.http import JsonResponse

def edit_image_dalle2(request):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    prompt = request.get('text', '')
    image_input = request.FILES.get('image')
    if not image_input:
        return JsonResponse({'error': 'No image file provided'}, status=400)
    
    image = None
    try:
        image = image_input.read()
    except Exception as e:
        # TODO handle specific exceptions
        print(e)
        return JsonResponse({'error': 'Failed to read image'}, status=400)
    try:
        
        response = client.images.edit(
            model='dall-e-2',
            image=image,
            prompt=prompt,
            n=1,
            size='1024x1024'
            )
        image_url = response.data[0].url
    except Exception as e:
        # TODO handle specific exceptions
        print(e)
        return JsonResponse({'error': 'Error calling api'}, status=500)
    
    return JsonResponse({'image_url': image_url}, status=200)



def change_image_dalle2(request):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    image_input = request.FILES.get('image')
    if not image_input:
        return JsonResponse({'error': 'No image file provided'}, status=400)
    
    image = None
    try:
        image = image_input.read()
    except Exception as e:
        # TODO handle specific exceptions
        print(e)
        return JsonResponse({'error': 'Failed to read image'}, status=400)
        
    try:
        response = client.images.create_variation(
            model="dall-e-2",
            image=image,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'Error calling api'}, status=500)
    
    return JsonResponse({'image_url': image_url}, status=200)



def gen_image_dalle3(request):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    prompt = request.get('text', '')
    
    try:
        response = client.images.generate(
            model='dall-e-2',
            prompt=prompt,
            size='1024x1024',
            quality='standard',
            n=1,
        )
        image_url = response.data[0].url
    except Exception as e:
        # TODO handle specific exceptions
        print(e)
        return JsonResponse({'error': 'Error calling api'}, status=500)
    
    return JsonResponse({'image_url': image_url}, status=200)
