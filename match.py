import streamlit as st
import joblib
import numpy as np

# تحميل النموذج
try:
    model = joblib.load("football_match_predictor_model.pkl")
except FileNotFoundError:
    st.error("❗ Model file not found. Please make sure 'football_match_predictor_model.pkl' exists.")
    st.stop()

# عنوان رئيسي
st.title("⚽ Football Match Outcome Predictor")
st.markdown("أدخل بيانات المباراة للتنبؤ بالنتيجة (فوز أو خسارة)")

# نموذج الإدخال
st.header("📊 Match Data Input")

rating_diff = st.number_input("Rating Difference", 
                              help="الفرق في التقييم العام بين الفريقين",
                              placeholder="مثال: 1.2")

possession_diff = st.number_input("Possession Difference", 
                                  help="الفرق في الاستحواذ بين الفريقين (%)",
                                  placeholder="مثال: 5.6")

goals_scored_diff = st.number_input("Goals Scored Difference", 
                                    help="الفرق في عدد الأهداف المسجلة",
                                    placeholder="مثال: 2")

net_goals_diff = st.number_input("Net Goals Difference", 
                                 help="الفرق الصافي للأهداف (المسجلة - المستقبلة)",
                                 placeholder="مثال: 1")

total_team_quality = st.number_input("Total Team Quality", 
                                     help="الجودة الإجمالية للفريق (تقييم داخلي)",
                                     placeholder="مثال: 85.0")

# زر التنبؤ
if st.button("🔍 Predict Result"):
    input_data = np.array([[rating_diff, possession_diff, goals_scored_diff, net_goals_diff, total_team_quality]])
    prediction = model.predict(input_data)[0]
    result = "🏆 Win" if prediction == 1 else "❌ Loss"
    st.success(f"🔮 Predicted Result: {result}")

