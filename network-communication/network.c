// network.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define BUFFER_SIZE 1024

void send_message(int sockfd, char *message) {
    send(sockfd, message, strlen(message), 0);
}

void receive_message(int sockfd, char *buffer) {
    recv(sockfd, buffer, BUFFER_SIZE, 0);
}

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr);

    connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr));

    char message[] = "Hello, Server!";
    send_message(sockfd, message);

    char buffer[BUFFER_SIZE];
    receive_message(sockfd, buffer);
    printf("Received message: %s\n", buffer);

    close(sockfd);
    return 0;
}
