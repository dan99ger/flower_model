# 🌸 Iris Flower Classification API (ML & Docker)

مشروع متكامل لتدريب نموذج تعلّم آلة ونشره كـ API باستخدام FastAPI وتغليفه عبر Docker.

## 🚀 التقنيات المستخدمة
- **Python 3.10**
- **Scikit-Learn** (Random Forest)
- **FastAPI & Uvicorn**
- **Docker**

## 🛠️ كيفية التشغيل
```bash
# 1. بناء الصورة
docker build -t iris-ml-api .

# 2. تشغيل الحاوية
docker run -d -p 8000:8000 --name iris_app iris-ml-api