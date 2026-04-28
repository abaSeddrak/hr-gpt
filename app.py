import streamlit as st
from openai import OpenAI
import os

# client = OpenAI(api_key="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")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("🧠 HR GPT System")

# -----------------------
# HR Policies (Simple Text)
# -----------------------
hr_policies = """
عدد الاجازات السنوية ٢١ يوم 
عدد الاجازات المرضية ١٤ يوم
ساعات العمل مرنه تبدء من ٨ ل ١٠ لحد ٤ ل ٦ 
فترة الاعداد ٣ شهور وبعدها يتم كتابة العقد 
نظام العمل عن بعد هو يوم واحد في
موشرات الاداء بتتاثر ب الحضور متاخر عن الميعاد لو 
في تاخير ربع ساعة يخصم ١٠٪ من قيمة اليوم
لو نص ساعة يخصم ٢٠٪ من قيمة اليوم
اكتر من ذلك يخصم نص يوم 
"""

st.subheader("HR Policies")
st.write(hr_policies)

# -----------------------
# Input
# -----------------------
question = st.text_input("Ask HR Question")

if question:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": f"""
You are HR assistant.
Answer only from HR policies below.
If not found say: "Not mentioned in policy"

POLICIES:
{hr_policies}
"""
            },
            {"role": "user", "content": question}
        ]
    )

    st.success(response.choices[0].message.content)