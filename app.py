import streamlit as st

st.title("Hello, IELTS/TOEFL Helper 👋")
st.write("输入题目后，我们将帮你生成结构化口语回答。")

# 下拉菜单
exam_type = st.selectbox("请选择考试类型：", ["IELTS Part2", "TOEFL Task1"])

question = st.text_input("请粘贴你的口语题目：")

verb_input = st.text_input("想用的动词（可多个，用英文逗号分隔，例如：travel, study, meet）：")
noun_input = st.text_input("想用的名词（同上，例如： friend, teacher, challenge）：")
adj_input = st.text_input("想用的形容词（同上，例如： exciting, difficult, useful）：")

#处理输入成列表

verbs = [v.strip()for v in verb_input.split(",")if v.strip()]
nouns = [n.strip()for n in noun_input.split(",")if n.strip()]
adjs = [a.strip()for a in adj_input.split(",")if a.strip()]

if st.button("生成口语答案"):
    if question and verbs and nouns and adjs:
        st.markdown("### 🗣️ 模拟回答")
        st.write(f"""
        Speaking of "{question}", I can’t help but think of how I once had to {verb} a/an {adj} {noun}.
        It was a time that really shaped me.
        """)
    else:
        st.warning("请先填写所有三个词，再点击生成。")