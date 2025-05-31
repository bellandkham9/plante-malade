from django.shortcuts import render
from django.shortcuts import render
from .models import Prediction
from .services.tflite_model import predict
from .models import Prediction

def home(request):
    return render(request, 'home.html')


def classify(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        predicted_class = predict(image_file)
        # Enregistrement
        prediction = Prediction.objects.create(
            image=image_file,
            predicted_class=predicted_class
        )


        return render(request, 'classify.html', {'prediction': prediction})
    return render(request, 'classify.html')



def historique_predictions(request):
    predictions = Prediction.objects.all().order_by('-predicted_at')  # plus récentes d'abord
    return render(request, 'history.html', {'predictions': predictions})
