<h2> 간단한 TCP 클라이언트 프로그램 구현 </h2>

- 프로그램 실행시,첫 번째 인자는 호스트명 또는 IP주소이며 두 번째 인자는 포트 번호이다.
- 사용자로부터 stdin (키보드)으로 문자열을 한 라인씩 입력받는다.
- 입력받은 라인의 마지막이 “\r\n”이 아니고, “\r” 없이 “\n”만 있는 경우는 “\n”을 “\r\n”으로 교체한다. 이 규칙은 라인이 “\n”인 경우에도 적용된다.
- 입력받은 라인을 서버로 전송한다.
- 서버로 전송 후에 이 입력받은 라인이 공백라인 (“\r\n” 또는 “\n”)인지를 검사하여, 공백라인이면 더 이상 입력을 받지 않는다.
- 이후 서버로부터 전송되는 내용을 화면으로 모두 출력한다.
- 예) 사용자로부터 받은 문자열 <br>
GET /web/index.html <br>
HTTP/1.1 <br>
Host: netapp.cs.kookmin.ac.kr <br>
Connection: Close <br><br>

<img width="481" alt="image" src="https://github.com/yoon-mina/socketprog/assets/143046108/69134940-4ec9-48cf-a7b6-770421e856b9">
