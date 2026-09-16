import streamlit as st
import requests

# 1. عنوان الصفحة وإعداداتها
st.set_page_config(page_title="Iris Predictor", page_icon="🌸", layout="centered")

st.title("🌸 تطبيق التنبؤ بنوع زهرة السوسن")
st.write("أدخل مقاسات الزهرة أدناه للحصول على التنبؤ المباشر من النموذج:")

st.divider()

# 2. إنشاء حقول المدخلات (Sliders)
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("طول الكأس (Sepal Length)", 4.0, 8.0, 5.1)
    sepal_width = st.slider("عرض الكأس (Sepal Width)", 2.0, 4.5, 3.5)

with col2:
    petal_length = st.slider("طول التويج (Petal Length)", 1.0, 7.0, 1.4)
    petal_width = st.slider("عرض التويج (Petal Width)", 0.1, 2.5, 0.2)

st.divider()

# 3. زر إرسال الطلب إلى الـ API
if st.button("🚀 التنبؤ بنوع الزهرة", use_container_width=True):
    # تجهيز البيانات كـ JSON
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    
    try:
        # إرسال طلب POST إلى الـ API
        response = requests.post("http://localhost:8000/predict", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            predicted_class = result.get("predicted_class", "غير معروف")
            
            st.success(f"🎉 **النتيجة المتوقعة:** {predicted_class.upper()}")
        else:
            st.error("حدث خطأ أثناء الاتصال بالـ API. تأكد من أن حاوية Docker تعمل.")
            
    except Exception as e:
        st.error(f"عذرًا، تعذر الاتصال بالخادم: {e}")