from django.shortcuts import render
import sklearn
import pandas as pd
import numpy as np
import pickle
# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def result(request):
    ph = request.POST.get('ph', None)
    Hardness = request.POST.get('Hardness', None)
    Solids = request.POST.get('Solids', None)
    Chloramines = request.POST.get('Chloramines', None)
    Sulfate = request.POST.get('Sulfate', None)
    Conductivity = request.POST.get('Conductivity', None)
    Organic_carbon = request.POST.get('Organic_carbon', None)
    Trihalomethanes = request.POST.get('Trihalomethanes', None)
    Turbidity = request.POST.get('Turbidity', None)

    query = [ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]

    with open('D:/College/DWM/WQA/water_quality_analysis/base/water_quality_pkl' , 'rb') as f:
        model = pickle.load(f)
    
    prediction = model.predict([query])
    context = {'result': prediction}

    return render(request, 'base/result.html', context=context)
