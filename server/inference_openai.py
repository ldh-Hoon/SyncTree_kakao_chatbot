from threading import Thread
from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import torch
import gradio as gr
import re
import asyncio
import requests
import shutil
from langchain import PromptTemplate, LLMChain
from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain.retrievers import ContextualCompressionRetriever
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain.llms import OpenAI

llm = OpenAI(model_name='gpt-3.5-turbo-instruct')

torch_device = "cuda" if torch.cuda.is_available() else "cpu"
print("Running on device:", torch_device)
print("CPU threads:", torch.get_num_threads())

loader = PyPDFLoader("total.pdf")
pages = loader.load()

# 데이터를 불러와서 텍스트를 일정한 수로 나누고 구분자로 연결하는 작업
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=0)
texts = text_splitter.split_documents(pages)

print(f"문서에 {len(texts)}개의 문서를 가지고 있습니다.")

# 임베딩 모델 로드
embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")

# 문서에 있는 텍스트를 임베딩하고 FAISS 에 인덱스를 구축함
index = FAISS.from_documents(
	documents=texts,
	embedding=embeddings,
	)

# faiss_db 로 로컬에 저장하기
index.save_local("")

# faiss_db 로 로컬에 로드하기
docsearch = FAISS.load_local("", embeddings)

embeddings_filter = EmbeddingsFilter(
    embeddings=embeddings,
    similarity_threshold=0.7,
    k = 2,
)
# 압축 검색기 생성
compression_retriever = ContextualCompressionRetriever(
	# embeddings_filter 설정
    base_compressor=embeddings_filter,
    # retriever 를 호출하여 검색쿼리와 유사한 텍스트를 찾음
    base_retriever=docsearch.as_retriever()
)


id_list = []
history = []
customer_data_list = []
context = "{context}"
question = "{question}"

def gen(x, id, customer_data):

    index = 0
    matched = 0
    count = 0
    for s in id_list:
        if s == id:
            matched = 1
            break;
        index += 1

    if matched == 0:
        index = len(id_list)
        id_list.append(id)
        customer_data_list.append(customer_data)
        history.append('상담원:무엇을 도와드릴까요?\n')

        bot_str = f"현재 고객님께서 가입된 보험은 {customer_data}입니다.\n\n궁금하신 것이 있으신가요?"
        return bot_str
    else:
        if x == "초기화":
            customer_data_list[index] = customer_data
            history[index] = '상담원:무엇을 도와드릴까요?\n'
            bot_str = f"대화기록이 모두 초기화되었습니다.\n\n현재 고객님께서 가입된 보험은 {customer_data}입니다.\n\n궁금하신 것이 있으신가요?"
            return bot_str
        elif x == "가입정보":
            bot_str = f"현재 고객님께서 가입된 보험은 {customer_data_list[index]}입니다.\n\n궁금하신 것이 있으신가요?"
            return bot_str
        else:
            context = "{context}"
            question = "{question}"
            customer_data_newline = customer_data_list[index].replace(",","\n")

            prompt_template = f"""당신은 보험 상담원입니다. 아래에 질문과 관련된 약관 정보, 응답 지침과 고객의 보험 가입 정보, 고객과의 상담기록이 주어집니다. 요청을 적절히 완료하는 응답을 작성하세요.
{context}
### 명령어:
다음 지침을 참고하여 상담원으로서 고객에게 필요한 응답을 간결하게 제공하세요.
[지침]
1.고객의 가입 정보를 꼭 확인하여 고객이 가입한 보험에 대한 내용만 제공하세요.
2.고객이 가입한 보험이라면 고객의 질문에 대해 적절히 답변하세요.
3.고객이 가입하지 않은 보험의 보상에 관한 질문은 관련 보험을 소개하며 보상이 불가능하다는 점을 안내하세요.
4.고객이 가입하지 않은 보험은 가입이 필요하다고 보험명을 확실하게 언급하세요.
다음 입력에 주어지는 고객의 보험 가입 정보와 상담 기록을 보고 고객에게 도움되는 정보를 제공하세요. 차근차근 생각하여 답변하세요. 당신은 잘 할 수 있습니다.
### 입력:
[고객의 가입 정보]
{customer_data_newline}
[상담 기록]
{history[index]}
고객:{question}
### 응답:
"""

            # RetrievalQA 클래스의 from_chain_type이라는 클래스 메서드를 호출하여 질의응답 객체를 생성
            qa = RetrievalQA.from_chain_type(
              llm=llm,
              chain_type="stuff",
              retriever=compression_retriever,
              return_source_documents=False,
              verbose=True,
              chain_type_kwargs={"prompt": PromptTemplate(
                  input_variables=["context","question"],
                  template=prompt_template,
              )},
            )
            query=f"나는 현재 {customer_data_list[index]}만 가입한 상황이야. {x}"
            response = qa({"query":query})
            output_str = response['result'].rsplit(".",1)[0]+"."
            print(prompt_template + output_str) 
            history[index] += f"고객:{x}\n상담원:{output_str}\n"
            return output_str
def reset_textbox():
    return gr.update(value='')
with gr.Blocks() as demo:
    gr.Markdown(
       "duplicated from beomi/KoRWKV-1.5B, baseModel:Llama-2-ko-7B-chat-gguf-q4_0"
    )

    with gr.Row():
        with gr.Column(scale=4):
            user_text = gr.Textbox(
                placeholder='입력',
                label="User input"
            )
            model_output = gr.Textbox(label="Model output", lines=10, interactive=False)
            button_submit = gr.Button(value="Submit")
        with gr.Column(scale=1):
            id_text = gr.Textbox(
                placeholder='772727',
                label="User id"
            )
            customer_data = gr.Textbox(
                placeholder='(무)1년부터저축보험, (무)수술비보험',
                label="customer_data"
            )
    button_submit.click(gen, [user_text, id_text, customer_data], model_output)
    demo.queue().launch(enable_queue=True)
