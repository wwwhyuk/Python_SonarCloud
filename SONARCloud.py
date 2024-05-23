import subprocess

# 명령어 및 옵션 설정
command = [
    r"D:\python\sonar-scanner-cli-5.0.1.3006-windows\sonar-scanner-5.0.1.3006-windows\bin\sonar-scanner.bat",
    "-Dsonar.organization=wwwhyuk",
    "-Dsonar.projectKey=wwwhyuk_Python_SonarCloud",
    "-Dsonar.sources=.",
    "-Dsonar.host.url=https://sonarcloud.io",
    "-Dsonar.python.version=3.11"
]

# 명령어 실행
try:
    subprocess.run(command, shell=True, check=True)
    print("소나클라우드 스캔이 성공적으로 실행되었습니다.")
except subprocess.CalledProcessError as e:
    print("소나클라우드 스캔을 실행하는 도중 오류가 발생하였습니다:", e)
