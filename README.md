1. SonarCloud 가입
2. Github Repository 생성
3. 생성한 Repo 를 SonarCloud 와 연결
4. Cloud 로컬 기반으로, SonarScanner-cli 다운
5. .git/workflows 과 sonar-project.properties 생성 및 내용 작성
6. 최초 commmit & push 또는 기존의 git 프로젝트 commit & push
7. 환경 변수에 Sonar Cloud 변수값 2개 ( Sonar Cloud 접속 시, 나타나는 환경 변수 2 가지 )
8. 프로젝트 cmd 경로에서 아래 command 실행 (sonar-scanner.bat 파일을 자신의 경로 맞춰 수정)
   ->D:\python\sonar-scanner-cli-5.0.1.3006-windows\sonar-scanner-5.0.1.3006-windows\bin\sonar-scanner.bat  -D"sonar.organization=wwwhyuk" -D"sonar.projectKey=wwwhyuk_Python_SonarCloud" -D"sonar.sources=." -D"sonar.host.url=https://sonarcloud.io" -D"sonar.python.version=3.11"
9. Sonar Cloud 에서 관련 정보 확인
