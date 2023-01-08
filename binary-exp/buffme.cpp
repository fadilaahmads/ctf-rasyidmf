#include <iostream>
#include <cstring>
int main() {
    int target;
    char buff[24];

    printf("Welcome to CTFR\n");
    printf("Welcome to Bufferoverflow, your buffer size is a way to decode flag inside this app!\n");
    printf("Please Input :");

    target = 0;
    fgets(buff);
    if (target != 0) {
        printf("Here is your flag : CTFR{REDACTED}\n");
    } else {
        printf("You are still not buffering this!\n", buff);
    }
    return 0;
}
