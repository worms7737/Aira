## Quick Navigation
[Version 1](#v1-1) | [Version 2](#v2-1) | [Version 3](#v3-1)

# Aira
Develop the Aira Chat Bot in Goorm 

# V1 [↑ Back to Top](#quick-navigation)

## 💠 **Aira - 클라우드 퍼포먼스 최적화 프로젝트** 💠

## **💠 프로젝트 개요**

### **프로젝트 소개**
Aira는 클라우드 퍼포먼스 최적화를 목표로 개인화된 AI 챗봇 서비스를 제공합니다. 트래픽 부하 분산, 자동 리소스 관리, 실시간 성능 모니터링을 통해 고가용성과 효율성을 극대화하는 클라우드 환경에서 운영됩니다.

### **프로젝트 목표**
1. 개발 및 운영 환경에서의 Load Balancing 및 Scaling 테스트 실행  
2. 실시간 모니터링 시스템과 경보 설정을 통한 운영 효율성 향상  
3. 클라우드 환경에서의 성능 저하 문제 분석 및 최적화 방안 연구  
 
---

### **지원 기능**
- 사용자 성향에 맞춤형 대화 서비스  
- 트래픽 변화에 따른 서버 증감 및 자동 복구  
- 시스템 리소스 상태 및 장애 발생 시 경고  

---

## **💠 역할 분담**

![image](https://github.com/user-attachments/assets/3075c3de-a2ea-4b79-9075-279c481142d1)

### **이영범 (팀장)**
- 이메일: yblee94@outlook.com  
- 역할:  
  - 프로젝트 총괄 관리, 일정 및 태스크 관리  
  - 프로젝트 기획 및 아이템 선정 주도  
  - 아키텍처 구축 리드  

### **오재근 (부팀장)**
- 이메일: worms773789@gmail.com  
- 역할:  
  - Backend 개발 리드  

### **김상아**
- 이메일: cometokr1@naver.com  
- 역할:  
  - 모니터링 구축 리드  
  - FrontEnd 개발 리드  

---
## **🗓️ 프로젝트 기간**

| 구분 | 기간 | 활동 |
|-------|-------|-------|
| 아이템 선정 및 프로젝트 기획 | 24.12.06 - 24.12.13 | - 프로젝트 기획 및 주제 선정<br>- 기획안 작성|
| 인프라 아키텍처 구축 | 24.12.16 - 24.12.20 | - EC2 인스턴스로 FE/BE 서버 구축<br>- MySQL DB 클러스터 및 인스턴스 구축<br>- Redis 엔진 활용 및 NoSQL DB 구축<br>- 스토리지 구축 |
| 기능1 구현 | 24.12.16 - 25.01.08 | - 엔드 유저 대상 질문 및 응답 저장 기능 구현 |
| 기능 2,3 구현 | 24.12.19 - 25.01.08 | - 설문 종료 후 사용자의 챗봇 유형 출력<br>- 웹 페이지 구현 |
| 모니터링 구축 | 24.12.10 - 25.01.08 | - 실시간 모니터링 서비스 구축<br>- EC2 인스턴스를 활용하여 CloudWatch와 Prometheus 구축 |
| 모니터링 시각화 | 25.01.06 - 25.01.10 | - EC2 인스턴스로 Grafana 대시보드 구축<br>- CloudWatch로 EC2 인스턴스 활용 경보 설정 및 Grafana 대시보드 구축 |
| 로드 부하 테스트 실행 | 25.01.09 - 25.01.13 | - EC2 인스턴스로 Locust 구축<br>- Locust로 테스트 시나리오 실행 |
| 클라우드 퍼포먼스 최적화 | 25.01.09 - 25.01.13 | - 성능 저하 문제점 분석 및 해결방안 도출<br>- Grafana 대시보드를 통한 성능 저하 병목현상 분석<br>- 리소스 병목현상에 적절한 솔루션 적용 |
| 최종 보고 | 25.01.13 - 25.01.15 | -완료 보고 PPT 제작 및 발표 준비 |


---

## **💠 사용 스택**

![24 12 12_jaksim_skillset_V4](https://github.com/user-attachments/assets/1af3704b-1b2f-4b66-a695-71eb070ecf1f)

### **Backend**
- FastAPI, Python, Uvicorn, OpenAI API  

### **Frontend**
- HTML, CSS, JavaScript, Bootstrap  

### **Database**
- Amazon Aurora (MySQL 호환), Redis (Elasticache)  

### **Infra**
- AWS EC2, VPC, AutoScaling, Ubuntu, Docker  

### **Monitoring & Test**
- CloudWatch, Prometheus, Grafana, Locust  

### **Storage**
- Amazon EFS, S3  

### **CI/CD**
- GitHub Actions  

### **Tools**
- Git, GitHub, Vscode, Discord, Notion, Clickup, Dockerhub  

---

## **🛠️ Service Architecture**

![image](https://github.com/user-attachments/assets/2159b988-6ec5-40ba-b318-249c219a58b3)

1. 엔드 유저의 Aira Web URL 접속
2. ELB(Elastic Load Balancer)를 통해 현재 트래픽 부하가 발생하지 않은 FE Server로 연결
3. 엔드 유저가 연결된 웹 서버는 정적 웹사이트 페이지를 S3 Bucket에서 불러와 엔드 유저에게 서비스
<br> 3.1 정적 콘텐츠는 S3 버킷 스토리지에 저장됨
4. FE Server를 타겟 그룹으로 생성된 Auto Scaling 그룹은 발생하는 트래픽 요청에 따라 자동으로 서버를 줄이거나 확장
5. 엔드 유저에게 서비스하는 동적 어플리케이션을 수행하기 위해 Elastic Load Balancer가 트래픽 부하가 발생하지 않은 BE Server로 연결
6. BE Server에서 서비스하는 어플리케이션을 엔드 유저는 수행
<br> 6.1 어플리케이션 Data는 EFS(Elastic File System)을 통해 BE Server 간에 동기화
7. BE Server를 타겟 그룹으로 생성된 Auto Scaling 그룹은 발생하는 트래픽 요청에 따라 자동으로 서버를 줄이거나 확장
8. 어플리케이션을 통해 수집된 고객 응답 데이터는 Aurora(MySQL호환) 데이터베이스에 저장, 엔드 유저의 세션 데이터는 Redis 엔진을 사용하는 Elasticache에 저장
9. 데이터베이스는 Multi-AZ 기능을 활용해 설정한 여러 가용영역에 복제하여 재해 상황 대비
10. CloudWatch 및 Prometheus를 활용하여 App 가동 중 발생하는 로그 데이터 및 운영 상황 모니터링 및 수집
11. Grafana를 활용해 데이터 시각화

---

## 설치

Create and activate a <a href="https://fastapi.tiangolo.com/virtual-environments/" class="external-link" target="_blank">가상 환경</a> 셋팅 이후 FASTAPI 설치:

<div class="termy">

```console
$ pip install "fastapi[standard]"

---> 100%
```

</div>

---

### 실행

서버 실행하기:

<div class="termy">

```console
$ fastapi dev main.py

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

---

---

# V2 [↑ Back to Top](#quick-navigation)

## 💠 **자동 오류 감지와 트랜잭션 무결성 클라우드 엔지니어링** 💠

## 💠 프로젝트 개요

### 프로젝트 소개
본 프로젝트는 트랜잭션 무결성과 클라우드 운영 안정성을 보장하기 위한 엔지니어링 솔루션을 제공합니다. 자동 오류 감지, SQS 기반의 메시지 처리, 모니터링 및 비용 최적화를 통해 고가용성과 효율적인 클라우드 환경을 구현했습니다.

### 프로젝트 목표
1. 트랜잭션 무결성 확보를 위한 FIFO Queue 기반 구조 설계  
2. 오류 감지 및 재처리를 위한 DLQ 및 알림 시스템 구축  
3. 클라우드 인프라 비용 최적화를 위한 ECS+Fargate, VPC 엔드포인트, Auto Scaling 도입  
4. 자동화된 CI/CD 파이프라인 구축 및 코드 품질 관리  

---

### 지원 기능
- 로그인 및 회원가입 기능  
- 사용자 데이터 수집 페이지  
- 정적/동적 리소스를 분리하여 효율적 서비스 제공  
- 오류 발생 시 자동 탐지 및 알림 전송  
- SQS를 활용한 비동기 메시지 처리 구조  
- Prometheus + Grafana 기반 실시간 모니터링  

---

## 💠 역할 분담

| 이름 | 역할 |
|------|------|
| 이영범 (팀장) | 프로젝트 총괄, AWS 아키텍처 설계 및 관리 |
| 오재근 (부팀장) | Backend 개발 리드, 트랜잭션 무결성 구현 |
| 김상아 | 모니터링 및 CI/CD 파이프라인 구축, 프론트엔드 개발 |

---

## 🗓️ 프로젝트 기간

| 구분 | 기간 | 활동 |
|------|------|------|
| 프로젝트 기획 | 24.12.06 - 24.12.13 | 기존 프로젝트 분석 및 확장 방향 도출, 아키텍처 설계 초안 작성 |
| 기능 구현 | 24.12.13 - 25.01.08 | 로그인, 회원가입, 사용자 데이터 수집, SQS 큐 기반 메시징 시스템 구현 |
| 클라우드 아키텍처 구성 | 24.12.13 - 25.01.10 | ECS+Fargate 기반 분산 아키텍처 구축, Route 53, ALB, Auto Scaling 설정 |
| 모니터링 구축 | 24.12.20 - 25.01.12 | Prometheus, Grafana, CloudWatch 설정 및 시각화 대시보드 구성 |
| CI/CD 자동화 | 25.01.03 - 25.01.13 | GitHub Actions, ESLint, flake8 적용 및 배포 자동화 |
| 최종 보고 | 25.01.13 - 25.01.15 | 결과 발표 자료 제작 및 시연 영상 촬영 |

---

## 💠 사용 스택

### Backend
- FastAPI, Python, OpenAI API, SQS

### Frontend
- HTML, CSS, JavaScript, Bootstrap

### Infra
- AWS ECS, Fargate, ALB, Route 53, VPC, Security Group

### Monitoring & Test
- CloudWatch, Prometheus, Grafana, Locust

### Storage
- Amazon S3, EFS

### CI/CD
- GitHub Actions, ESLint, flake8

### Tools
- Git, GitHub, VSCode, Docker, Notion, Discord

---

## 🛠️ Service Architecture

1. 사용자는 Route 53을 통해 HTTPS 기반으로 서비스 접속  
2. ALB를 통해 프론트 컨테이너(Fargate)에 트래픽 전달  
3. 프론트 컨테이너는 S3+CloudFront 기반 정적 자원 서비스  
4. 백엔드 요청은 ALB를 통해 Backend ECS로 전달  
5. GPT 컨테이너는 퍼블릭 서브넷에서 ALB와 연결되어 응답 처리  
6. SQS를 통해 요청/응답 메시지를 비동기적으로 처리하고, DLQ를 통해 오류 발생 시 알림 전송  
7. Prometheus, Grafana를 통해 실시간 로그 모니터링 수행  
8. .env는 EFS에 저장되고, S3는 내부 VPC Endpoint를 통해 접근  
9. CI/CD는 GitHub Actions를 통해 자동화, 빌드된 Docker 이미지를 ECR에 배포 후 ECS에 자동 반영  

---

## 설치

```bash
# 가상 환경 설정 후 FastAPI 설치
pip install "fastapi[standard]"
```

---

## 실행

```bash
# 개발 서버 실행
fastapi dev main.py
```
"""

---

---

# V3 [↑ Back to Top](#quick-navigation)

## 💠 **IaaS 클라우드 운영 자동화 프로젝트** 💠

## 💠 프로젝트 개요

### 프로젝트 소개
작심3팀은 IaaS 클라우드 환경의 운영 및 관리를 자동화하기 위해 IaC(Infrastructure as Code) 도구와 CI/CD 도구를 활용한 클라우드 네이티브 엔지니어링 프로젝트를 수행했습니다.  

개인화된 챗봇 Aira를 기반으로, 클라우드 인프라 자동 구축, 모니터링, 비용 관리, 자동 확장 및 백업/복구까지 자동화된 운영이 가능하도록 설계하였습니다.

### 프로젝트 목표
1. Terraform, Ansible을 이용한 인프라 구성 자동화  
2. GitHub Actions, ArgoCD를 활용한 CI/CD 파이프라인 구축  
3. 예산 초과 자동 알림 및 불필요 자원 제거를 통한 비용 최적화  
4. 클러스터 모니터링 및 Auto Scaling 적용  
5. SQS, CronJob을 활용한 데이터 백업 및 복구 자동화  

---

## 💠 역할 분담

| 이름 | 역할 |
|------|------|
| 이영범 (팀장) | 프로젝트 기획, Terraform 기반 인프라 구성 |
| 오재근 (부팀장) | Ansible 자동화, 백업 및 복구 로직 구성 |
| 김상아 | CI/CD 파이프라인 구축, 모니터링 시스템 구현, 문서 작성 |

---

## 🗓️ 프로젝트 기간

| 주차 | 활동 |
|------|------|
| Week 1 | 요구사항 정의 및 아키텍처 설계 |
| Week 2 | 기존 ECS 인프라를 EKS로 전환 |
| Week 3 | Terraform, Ansible을 활용한 인프라 구성 |
| Week 4 | GitHub Actions + Argo CD를 통한 CI/CD 파이프라인 구축 |
| Week 5 | Prometheus, Grafana를 통한 모니터링 및 자동 확장 구현, 백업/복구 테스트 |

---

## 💠 사용 스택

### IaC
- Terraform: EKS 클러스터 및 워커 노드 구성
- Ansible: ArgoCD, Monitoring 등 네임스페이스 및 설정 자동화

### CI/CD
- GitHub Actions
- ArgoCD (GitOps 방식 적용)

### Monitoring & Alert
- Prometheus, Grafana, CloudWatch

### Storage & Backup
- Amazon S3, SQS(FIFO 큐), DLQ, CronJob

### 테스트 및 품질 관리
- Jest, Pytest, ESLint, Flake8, Docker Scout, Trivy, Dependabot

---

## 🛠️ 주요 구현 내용

### ✅ IaC 자동화
- Terraform으로 EKS 클러스터 초기 설정 자동화
- Ansible로 모듈화된 플레이북 작성 → ArgoCD 및 모니터링 도구 자동 설치

### ✅ CI/CD 파이프라인
- GitHub Actions를 통한 코드 빌드, 테스트, 보안 검사, 이미지 빌드 자동화
- ArgoCD를 활용한 GitOps 방식 Kubernetes 배포 자동화

### ✅ 비용 관리 자동화
- 월 $150 초과 시 이메일 알림 설정 (예산 초과 시 빠른 대응)
- Cost Explorer 활용 실시간 비용 모니터링
- 필요 시 클러스터 자동 제거로 비용 절감

### ✅ 모니터링 및 Auto Scaling
- CPU, 메모리, 디스크, 네트워크 등 주요 지표 실시간 수집 및 시각화
- 장애 발생 시 로드밸런싱 + 자동 복구 구성

### ✅ 데이터 백업 및 복구
- SQS(FIFO) 큐를 통한 메시지 무결성 보장
- CronJob으로 매일 새벽 자동 백업 및 수동 복구 테스트 성공
- 백업 SQL을 기반으로 MySQL 복원 성공

---

## 설치 및 실행

```bash
# Terraform 실행
terraform init
terraform apply

# Ansible 플레이북 실행
ansible-playbook -i inventory main.yml
```

```bash
# GitHub Actions를 통한 CI/CD 자동화
# 메인 브랜치 merge 시 배포 자동 실행
```

---

## 💡 주요 효과

- 수동 작업을 최소화한 운영 자동화 실현
- 클라우드 자원 낭비 최소화 및 예산 관리 자동화
- 신뢰성 높은 백업 및 복구 체계 구축
- 모니터링 + 자동 확장으로 안정성 높은 서비스 제공
"""

