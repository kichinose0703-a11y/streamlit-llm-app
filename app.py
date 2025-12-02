#from dotenv import load_dotenv

#load_dotenv()


from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def create_llm_answer(input_text,selected_item):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    if selected_item == "おすすめの映画を提案する専門家":
        question_text = f"おすすめの映画を教えてください。ジャンルは以下の通りです: {input_text}"
        
        messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=question_text),
        ]
    elif selected_item == "おすすめの曲を提案する専門家":
        question_text = f"おすすめの曲を教えてください。ジャンルは以下の通りです: {input_text}"
        
        messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=question_text),
        ]
    else:
        messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=input_text),
        ]

    result = llm(messages)

    return result.content


import streamlit as st

st.title("課題用アプリ: おすすめを提案するアプリ")

st.write("##### 動作モード1: おすすめの映画を提案する専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでおすすめの映画を回答します。")
st.write("##### 動作モード2: おすすめの曲を提案する専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことでおすすめの曲を回答します。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["おすすめの映画を提案する専門家", "おすすめの曲を提案する専門家"]
)

st.divider()

if selected_item == "おすすめの映画を提案する専門家":
    input_message = st.text_input(label="観たいジャンルを入力してください。")
else:
    input_message = st.text_input(label="聴きたいジャンルを入力してください。")


if st.button("実行"):
    st.divider()

    if selected_item == "おすすめの映画を提案する専門家":
        if input_message:
            llm_answer = create_llm_answer(input_message, selected_item)
            st.write(f"回答: **{llm_answer}**")
        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            llm_answer = create_llm_answer(input_message, selected_item)
            st.write(f"回答: **{llm_answer}**")
        else:
            st.error("テキストを入力してから「実行」ボタンを押してください。")