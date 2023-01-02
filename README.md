# 실시간 아동학대 알림 웹 사이트: 도담도담 🍼

어린이집 내 실시간 아동학대 알림 웹 사이트

### 배포 링크: ~~[도담도담 웹 사이트](http://3.39.165.135/)~~
> 현재 서버 비용 문제로 배포가 중지되었습니다.

## 프로젝트 개요

### 제안 배경
- 아동학대 신고 접수 건수에 보육 교사, 학교 교사에 의한 아동학대 사례가 다수이다.
- 어린이집 내 아동학대 사건 발생 후 고의적으로 CCTV를 망가뜨려 증거를 훼손할 수 있다.
- 어린이집 CCTV는 복잡한 절차로 인해 열람이 불가능해 처벌이 어려워진다.

### 프로젝트 목표
- 도담도담은 어린아이가 탈 없이 잘 놀고 잘 자라나는 모양이라는 순우리말로, 효과적인 아동 학대 예방 및 양육자에 대한 신뢰도 향상으로 인한 건강한 보육 환경을 조성을 목적으로 합니다.

### 수상
- 🏆 2022년 한이음 ICT 멘토링 공모전 수상
- 🏆 2022년 제 13회 세종대학교 창의설계경진대회 수상


## 프로젝트 기능
### 로그인 / 회원가입
- 회원가입한 사용자만 해당 서비스를 사용할 수 있습니다.
### 어린이집 등록
- 전국에 있는 모든 어린이집 정보를 공개된 [Open API](https://www.data.go.kr/data/15013108/standard.do)를 크롤링한 데이터를 통해 어린이집을 등록할 수 있습니다.
### 실시간 학대 알림
- 아동학대가 감지되면 학대 영상이 클라우드 스토리지에 업로드됩니다.
- 학대 행위가 검출된 영상을 사용자에게 실시간으로 제공합니다.
### 학대 행위 통계
- 학대 행위를 단계별로 통계를 제공합니다.

## 기술 스택

- **Front-End** <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=flat&logo=Vue.js&logoColor=white"> <img src="https://img.shields.io/badge/NGINX-009639?style=flat&logo=NGINX&logoColor=white">
- **Back-End** <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Redis-DC382D?style=flat&logo=Redis&logoColor=white"> <img src="https://img.shields.io/badge/Celery-37814A?style=flat&logo=Celery&logoColor=white"> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=SQLite&logoColor=white"><img src="https://img.shields.io/badge/Socket.io-010101?style=flat&logo=Socket.io&logoColor=white">
- **Deploy** <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white"> <img src="https://img.shields.io/badge/EC2-010101?style=flat&logo=EC2&logoColor=white"> <img src="https://img.shields.io/badge/AmazonS3-569A31?style=flat&logo=AmazonS3&logoColor=white">

 ## 📁 프로젝트 구조
 
 ```bash
capstone2022
├── backend               # 백엔드 코드들
├── frontend              # 프론트엔드 코드들
├── docker-compose.yml    # 도커 컴포즈 파일
└── ...이외 기타 파일들       # package.json을 비롯한 기타 파일들
```

 ### Frontend 구조
 
 ```bash
frontend
├── public                # index.html / favicon
└── src
    ├── api               # api 관련 모듈들
    ├── assets            # 필요한 리소스들
    ├── components        # 컴포넌트들
    ├── router            # 라우터들
    ├── store             # 상태관리
    ├── styles            # 공통 스타일들(base.scss)
    ├── utils             # 재사용 가능한 모듈들
    ├── views             # 페이지들
    ├── App.vue(FILE)     # App 컴포넌트
    └── main.js(FILE)     # entry point
```

 ### Backend 구조
 
 ```bash
backend
├── account               # 계정 관련 app
├── bin                   # 실행 스크립트
├── backend               # 환경변수 및 설정
├── center                # 어린이집 관련 app
├── notification          # 알림 관련 app
├── utils                 # 범용 함수, 클래스들
├── Dockerfile(FILE)      # 도커 파일
├── manage.py(FILE)       # command line 유틸리티
└── requriements.txt(FILE)# 설치 목록
```

 ## ▶️ 설치 및 실행
 
 ### 프로젝트 설치 및 실행 - Development mode
 #### client
.env 파일
```bash
VUE_APP_API_URLT=YOUR SERVER API
 ```
 실행
 ```bash
 npm install
 npm run serve
 ```
 
 ## 📘 Documents
 - [API](https://www.notion.so/API-d2e04d68815647699d0ce1800a87bcda)
 - [ERD](https://www.notion.so/ERD-291d5a3832c24b049f793ea4f21406ed)

## Demo
- Figma
- 기획서
- [발표 영상](https://www.youtube.com/watch?v=cUjmKBDj_mQ&t=24s)
