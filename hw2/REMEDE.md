<h2> 간단한 파일서버 구현 </h2>

- 특정 확장자를 가진 파일 목록 다운로드
- 주어진 이름의 파일 다운로드
- 파일업로드

1) GET filename: 이 명령이 들어오면 서버는 filename에 해당하는 파일을 찾아 서 tcp 연결을 통해 전송한다.<br>
만약 존재하지 않으면 "FILE NOT FOUND\r\n" 을 클라이언트로 전송한다.
2) PUT filename: 이 명령이 들어오면 서버는 filename 이라는 파일을 현재 디렉 토리에 생성한 후, 이 tcp 연결을 통해 명령 라인 이후에 들어오는 모든 내용을 이 filename 파일에 쓴다.
3) LS ext: 이 명령이 들어오면 서버는 현재 디렉토리에서 파일 확장자가 ext인 파일을 찾아서 tcp 연결을 통해 전송한다. <br>
전송시에는 한 라인에 한 파일명을 전송한다. <br>
구체적으로는 라인 구분을 “\r\n”으로 해서 각 파일에 대해서 “파 일명\r\n”의 형태로 전송하면 된다.
<br>

<img width="537" alt="image" src="https://github.com/yoon-mina/socketprog/assets/143046108/7016c30c-8bbc-4d79-b10a-503670481787">
<img width="612" alt="image" src="https://github.com/yoon-mina/socketprog/assets/143046108/6ba5b2d0-6370-486b-96d7-5d9dd914a24a">
<img width="421" alt="image" src="https://github.com/yoon-mina/socketprog/assets/143046108/444bc3c6-0e28-4f3a-b216-06aaf152d6a9">
