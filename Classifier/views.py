import django
from django.shortcuts import render
from django import forms
from django.views import View
import tensorflow as tf
from .models import ImageStore
import numpy as np
from keras.preprocessing import image
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
from django.conf import settings
import pickle
import pandas as pd

# Create your views here.
global loaded_model
loaded_model = pickle.load(open('Classifier\\trained_models\\finalized_model.sav', 'rb'))

def predict_from_symptoms(answers, model=loaded_model):
    x = pd.DataFrame(answers)
    print(model.predict_proba(np.asarray(x[0].values).reshape(1, -1)))
    chances_y = str(round(model.predict_proba(np.asarray(x[0].values).reshape(1, -1))[0][-1] *100,2)) + '%'
    chances_x = str(round(model.predict_proba(np.asarray(x[0].values).reshape(1, -1))[0][0] *100,2)) + '%'
    if model.predict(np.asarray(x[0].values).reshape(1, -1))[0] == 'Yes':
        return '<span style="color:red; font-size:30px"><b><i>Covid!</i></b></span><br><b><i>Chances: {}</i></b><br>This Classifier detected that you are Covid Positive <br> But honestly speaking that this classifier is based on old data so it\'s not so caccurate'.format(chances_y)
    else:
        return '<span style="color:red; font-size:30px"><b><i>Normal</i></b></span><br><b><i>Chances: {}</i></b><br>This Classifier detected that you are most probably Covid Negative <br> But honestly speaking that this classifier is based on old data so it\'s not so accurate'.format(chances_x)
  
class ImgForm(forms.ModelForm):
  
    class Meta:
        model = ImageStore
        fields = ['name', 'image']
        widgets= {
            'image': forms.FileInput(attrs={
                'class':'form-control',
                'id':'formFile'
            }),
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Give your image a name!'
            })
        }



global model
model = tf.keras.models.load_model('Classifier\\trained_models\\LossOptimized')




def predict_covid(imgUrl , model=model):
    model = model

    img = image.load_img(imgUrl, target_size=(250, 250))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images)
    encode_label = np.argmax(classes,axis=1)
    lb = {0: 'Covid', 1: 'Normal', 2: 'Pneumonia'}

    chances = str(max(classes.flatten().tolist())*100)[:4] + '%'
    encoded = str(lb[encode_label[0]])

    if encoded == 'Covid':
        statement = """Doctor Robo suggests that you might have <b><i>COVID 19</i><b> ! <br><b><i> But Doctor Robo is basically a software based on AI and is prone to error!
        Currently DOCTOR ROBO is for research purposes only! <br> So seek advice from your doctor</i><b> :)
        
        """
    elif encoded == 'Pneumonia':
        statement = """Doctor Robo suggests that you might have Viral Pneumonia in your lungs! <br><b><i> But Doctor Robo is basically a software based on AI and is prone to error!
        Currently DOCTOR ROBO is for research purposes only! <br> So seek advice from your doctor </i><b> :)
        
        """
    else:
        statement =  'As per DOCTOR ROBO\'s assessment your lungs are Normal but actually DOCTOR ROBO is based on AI and is prone to error!  <br> So seek advice from your doctor :)'

    return {
        'disease':'<span style="color:red;">'+encoded+'</span>',
        'chances':chances,
        'statement':statement,
        }

  
# Create your views here.
def image_view(request):
  
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('classifier:solver',request.POST['name'])
    else:
        form = ImgForm()
    return render(request, 'Classifier/index.html', {'form' : form})

def success(request):
    return HttpResponse('successfully uploaded')

def solver(request,name):
  
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        img = ImageStore.objects.get(name=name)
        url = settings.MEDIA_ROOT + '\\' + os.path.basename(img.image.url)
        x = predict_covid(url)
        img.delete()
        x['imgUrl'] = '/media/' + os.path.basename(img.image.url)
        return render(request, 'Classifier/xrayresult.html', x)

def symptoms(request):
    if request.method == 'GET':
        return render(request, 'Classifier/symptoms.html')
    elif request.method == 'POST':
            submitted_anwsers = {}
            for key in request.POST:
                if key != 'csrfmiddlewaretoken':
            
                    value = request.POST[key]
                    submitted_anwsers[key] = int(value)
            answers = submitted_anwsers.values()
            x = predict_from_symptoms(answers)
            v = {'statement_covid':x}
    return render(request,'Classifier/xrayresult.html',v)
        



