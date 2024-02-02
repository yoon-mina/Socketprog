<h2> 간단한 웹서버 구현 </h2>

- 웹브라우저 (구글 크롬 등 상용 웹브라우저를 사용함)를 실행해서 위 .html 파일, .txt 파일, .jpg 파일 중 하나를 요청한다.
- 이 때 URL은 아래와 같다. 같은 호스트에서 요청하기 때문에 도메인 네임은 localhost를 사용하였다.<br>
  http://localhost:10000/palladio.jpg
- 브라우저에 위 URL을 입력하고 엔터를 치면 palladio.jpg 파일을 서버로 요청하게 된다. hw3는 이 브라우저가 요청한 HTTP Request 메시지의 첫번째 라인과 Host를 제외한 모든 헤더 정보를 출력한다.
- 참고. 혹시 연결이 안될 경우 방화벽에서 10000 번 포트번호를 허용하도록 변경한다.
- 그리고, 해당하는 파일을 찾아서 HTTP Response 메시지로 만들어서 브라우저로 보낸다.
  
- hw3가 사용하는 HTTP Response 메시지는 아래와 같다. <br>
HTTP/1.0 200 OK <br>
Connection: close <br>
Content-Length: 142740 <br>
Content-Type: image/jpeg <br>

- 요청 파일이 html 일 경우는 아래와 같다. <br>
HTTP/1.0 200 OK <br>
Connection: close <br>
Content-Length: 20 <br>
Content-Type: text/html <br>

- 요청 파일이 txt 일 경우는 아래와 같다. <br>
HTTP/1.0 200 OK <br>
Connection: close <br>
Content-Length: 210 <br>
Content-Type: text/plain <br>

- Content-Length 헤더 필드에는 파일의 크기를 입력한다.
- 다 보내고 나면 실제 전송한 바이트 수와 파일의 바이트 수를 출력한다. <br>
File Transfer Done: Sent 3039179, File Size 3039179 <br>

- 이 두 값은 같아야 정상이다. 아래 화면은 이러한 내용을 보여준다. 
- “Host:” 헤더 필드는 없 는 것을 확인할 수 있다.
<br>

<img width="766" alt="image" src="https://github.com/yoon-mina/socketprog/assets/143046108/cfb10473-3106-4c34-9048-4f0e552fe672">
