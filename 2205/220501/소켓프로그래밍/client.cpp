#include <WinSock2.h>
#include <stdlib.h>
#include <stdio.h>

#define SERVERIP "127.0.0.1"
#define SERVERPORT 9000
#define BUFSIZE 512

int main(int argc, char *argv[]) {
	int retval;
	WSADATA wsa;
	if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) return 1;

	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);

	SOCKADDR_IN serveraddr;
	ZeroMemory(&serveraddr, sizeof(serveraddr));
	serveraddr.sin_family = AF_INET;
	serveraddr.sin_addr.s_addr = inet_addr(SERVERIP);
	serveraddr.sin_port = htons(SERVERPORT);
	connect(sock, (SOCKADDR*)&serveraddr, sizeof(serveraddr));

	char buf[BUFSIZE + 1];
	int len;

	while (1) {
		printf("\n[보낼 데이터] ");
		// 입력받아 server에게 전송
		if (fgets(buf, BUFSIZE + 1, stdin) == NULL) break;
		len = strlen(buf);
		if (buf[len - 1] == '\n') buf[len - 1] = '\0';
		if (strlen(buf) == 0) break;
		retval = send(sock, buf, strlen(buf), 0);
		printf("[TCP 클라이언트] %d바이트를 보냈습니다.\n", retval);
		
		retval = recv(sock, buf, BUFSIZE, 0);
		if (retval == 0) break;

		buf[retval] = '\0';
		printf("[TCP 클라이언트] %d바이트를 받았습니다.\n", retval);
		printf("[받은 데이터] %s\n", buf); 
	}

	closesocket(sock);

	WSACleanup();
	return 0;
}
