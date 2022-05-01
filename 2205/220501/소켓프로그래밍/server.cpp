#include <WinSock2.h>
#include <stdlib.h>
#include<stdio.h>

#define SERVERPORT 9000
#define BUFSIZE 512

int main(int argc, char* argv[]) {
	int retval;
	WSADATA wsa;
	if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
		return 1;
	}

	SOCKET listen_sock = socket(AF_INET, SOCK_STREAM, 0);

	SOCKADDR_IN serveraddr;
	ZeroMemory(&serveraddr, sizeof(serveraddr));
	serveraddr.sin_family = AF_INET;
	serveraddr.sin_addr.s_addr = htonl(INADDR_ANY); // 내 IP주소를 network서버 order로 변경하여 저장 
	serveraddr.sin_port = htons(SERVERPORT);
	bind(listen_sock, (SOCKADDR*)&serveraddr, sizeof(serveraddr));
	listen(listen_sock, SOMAXCONN); //하부 프로토콜의 최대의 큐의 크기로 동시에 받아들일 수 있도록한다.

	SOCKET client_sock;
	SOCKADDR_IN clientaddr;
	int addrlen;
	char buf[BUFSIZE + 1];
	int len;


	while (1) {
		addrlen = sizeof(clientaddr);
		client_sock = accept(listen_sock, (SOCKADDR*)&clientaddr, &addrlen);

		printf("\n[TCP 서버] 클라리언트 접속 : IP 주소 = %s, 포트 번호 = %d\n",
			inet_ntoa(clientaddr.sin_addr), ntohs(clientaddr.sin_port));

		while (1) {
			retval = recv(client_sock, buf, BUFSIZE, 0);
			buf[retval] = '\0';
			printf("\n[TCP %s : %d ] %s\n", inet_ntoa(clientaddr.sin_addr),
				ntohs(clientaddr.sin_port), buf);
			
			printf("\n[보낼 데이터] ");
			if (fgets(buf, BUFSIZE + 1, stdin) == NULL) break;

			len = strlen(buf);
			if (buf[len - 1] == '\n') buf[len - 1] = '\0';
			if (strlen(buf) == 0) break;

			retval = send(client_sock, buf, strlen(buf), 0);
		}

		closesocket(client_sock);
		printf("[TCP 서버] 클라이언트 종료 : IP 주소 =%s, 포트번호 = %d\n",
			inet_ntoa(clientaddr.sin_addr), ntohs(clientaddr.sin_port));
	}

	closesocket(listen_sock);
	WSACleanup();
	return 0;
}
