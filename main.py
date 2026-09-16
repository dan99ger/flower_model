from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
#تهيئة التطبيق وتحميل النموذج
app=FastAPI(title="Iris Flower Classification API", description="API لتوقع نوع الزهرة باستخدام نموذج التعلم الآلي", version="1.0.0")
model=joblib.load('rf_model.pkl')
scaler=joblib.load('scaler.pkl')

target_names = ['setosa', 'versicolor', 'virginica']

#تعريف هيكل البيانات المدخلة باستخدام Pydantic
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
@app.get("/")
def home():
    return {"message": "  مرحباً بك في واجهة تنبؤات نموذج تصنيف الزهور!"}
#نقطة النهاية لتوقع نوع الزهرة
@app.post("/predict")
def predict(data: IrisFeatures):
    input_data = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])
    #تطبيق التحجيم القياسي
    scaled_data = scaler.transform(input_data)
    #توقع نوع الزهرة 
    prediction = model.predict(scaled_data)[0]
    predicted_class = target_names[prediction]
    
    return {
        "prediction_index": int(prediction),
        "predicted_class": predicted_class
    }