#define _GNU_SOURCE         /* See feature_test_macros(7) */
#include <sys/mman.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "mybin.h"

int main(int argc, char **argv, char **env)
{
    int memfd = memfd_create("hello", 0);
    /* int memfd = open("mybin", O_RDWR); */
    if (memfd == -1)
	exit(84);
    size_t curPtr = 0;
    int d = 0;
    while (curPtr < BINARY_DATA_SIZE - 512)
    {
	write(memfd, &BINARY_DATA[curPtr], 512);
	curPtr += 512;
	d++;
    }
    int r;
    r = fexecve(memfd, argv, env);
	//You will have to create the argv and pass the envp argument from main
    perror(strerror(r));
    return 0;
}
