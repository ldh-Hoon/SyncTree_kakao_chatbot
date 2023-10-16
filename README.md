# 보험상담 kakao chatbot

![image](https://github.com/ldh-Hoon/SyncTree_kakao_chatbot/assets/139981434/c91bc235-13a5-4b20-a9e8-070df1b4bb7c) ![image](https://github.com/ldh-Hoon/SyncTree_kakao_chatbot/assets/139981434/de05c641-68c4-4058-be2a-537b194fd457)

![image](https://github.com/ldh-Hoon/SyncTree_kakao_chatbot/assets/139981434/b21d62ea-47a7-4544-b409-c161a34956ff) ![image](https://github.com/ldh-Hoon/SyncTree_kakao_chatbot/assets/139981434/d278ceeb-5f28-4ed3-9b11-61a3ed0c4c2a)




싱커톤 시즌3 참가 결과물 설명페이지입니다.

[Synctree 싱커톤](https://www.synctree101.com/syncathon/main)https://www.synctree101.com/syncathon/main

Demo:
챗봇 링크(채널링크 추가)

영상:
유튜브 링크 추가

### 개요

기존 교보 라이프스타일 카카오 챗봇을 개선하여 자율적인 응답이 가능합니다.

openai gpt3.5가 보험 약관 문서를 참고하여 답변해줍니다.

교보 라이프스타일 api블록을 통해 가입 정보를 불러와 답변에 참고합니다.

현재 gpt 무료 크레딧 제한으로 같이 입력되는 약관 pdf의 내용이 다소 적게 설계되어 있습니다. 

개선 시 답변이 더 좋아질 여지가 남아있습니다.

### 스샷 

### 구조
싱크트리 백엔드
Huggingface langchain inference server
카카오톡 챗봇
