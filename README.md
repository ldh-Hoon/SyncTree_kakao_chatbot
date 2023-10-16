# 보험상담 kakao chatbot

![image](https://github.com/ldh-Hoon/SyncTree_kakao_chatbot/assets/139981434/48d14936-79bc-4cbc-9deb-253837d7ba3d)


[싱커톤 시즌 3](https://www.synctree101.com/syncathon/main) 참가 결과물 설명페이지입니다.


Demo:
[챗봇 링크](http://pf.kakao.com/_xoxmZCG/chat)

영상:
유튜브 링크 추가

## 📆프로젝트 기간 

2023.10.4 - 2023.10.17



## 개요

기존 교보 라이프스타일 카카오 챗봇을 개선하여 자율적인 응답이 가능합니다.

openai gpt3.5가 보험 약관 문서를 참고하여 답변해줍니다.

교보 라이프스타일 api블록을 통해 가입 정보를 불러와 답변에 참고합니다.

현재 gpt 무료 크레딧 제한으로 같이 입력되는 약관 pdf의 내용이 다소 적게 설계되어 있습니다. 

개선 시 답변이 더 좋아질 여지가 남아있습니다.

## 스샷 

## 구조
싱크트리 백엔드
Huggingface langchain inference server
카카오톡 챗봇
