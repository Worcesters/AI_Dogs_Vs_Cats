from django.http import JsonResponse
import json
from requests import request
from .models import History


def load_image(request):
    if request.method == 'POST':
        import re
        import base64
        import os
        from PIL import Image
        from keras.preprocessing.image import ImageDataGenerator
        from tensorflow import keras
        import tensorflow as tf
        from keras.preprocessing.image import load_img
        from keras.preprocessing.image import img_to_array
        

        data = json.loads(request.body)
        pattern = '(png|jpg|jpeg)'
        extension = re.findall(pattern, data['img_name'])
    
        # Extension verification
        if(len(extension) != 0):
            #load model
            model = keras.models.load_model('dogs_vs_cats/models/model_dog_cat')

            # Nettoyage du code Base64 "data:image\png;base64,xxxxxxxx"
            clean = re.sub('^data:image\/(png|jpg|jpeg);base64,', '', data['img_loaded'])

            # Image Nettoyer et Decoder
            image = base64.b64decode(clean)

            # Enregistrement de l'image sous format fichier 
            file = data['img_name']
            with open(file, "wb") as f:
                f.write(image)

            # Load the image
            img = load_img(file, target_size=(150, 150))

            # Convert to array
            img = img_to_array(img)
            
            # Reshape into a single sample with 3 channels
            img = img.reshape(1, 150, 150, 3)
            pred = model.predict(img)

            if(pred[0][0] == 0):
                result = 'Chat'
            elif(pred[0][0] == 1):
                result = 'Chien'
            else:
                result = "Qu'est ce que ?.?"

            # Enregistrement de l'image, du resultat et du nom dans la bdd
            cH = History.objects.create(image=clean, name=data['img_name'], result=result)
            cH.save()

            # Suppression du fichier image dans les dossiers
            os.remove(data['img_name'])
            
            sortie = []
            sortie.append({'result':result, 'image':data['img_loaded'], 'id':cH.id})
            
            if(result):
                return JsonResponse({'error': False, 'data': sortie})
            else:
                return JsonResponse({'error': True, 'message': 'no result found'})

        else:
            return JsonResponse({'error': True, 'message': 'bad file extension'})
    else:
        return JsonResponse({'error': True, 'message': 'bad request'})

def errorReport(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        try:
            # Enregistrement de l'image, du resultat et du nom dans la bdd
            History.objects.filter(id = data['id']).update(error=True)
            return JsonResponse({'error': False, 'message': 'Vous avez bien signalé que le resultat est faux, Merci de votre aide !'})
        except History.DoesNotExist:
            return JsonResponse({'error': True, 'message': 'fatal error'})
    else:
        return JsonResponse({'error': True, 'message': 'bad request'})