#define _GNU_SOURCE         /* See feature_test_macros(7) */
#include <sys/mman.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <stdarg.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "constant.h"
#include "mybin.h"

char **fill_args(char **wordtab, int nb, char *format, ...)
{
	va_list ap;

	va_start(ap, format);
	for (int i = 0; i < nb; i++) {
		wordtab[i] = va_arg(ap, char *);
	}
	va_end(ap);
	return wordtab;
}

int main(int argc, char **argv, char **env)
{
	/* Create a temporary file that will contain the program */
	int memfd = memfd_create("mybin", MFD_ALLOW_SEALING);

	/* Check if memfd_create succeded */
	if (memfd == -1)
	{
		perror("Error :");
		exit(84);
	}

	/* Check if bin2c files are viable */
	if (BINARY_DATA_SIZE == 0)
	{
		perror("BINARY_DATA_SIZE is NULL");
		exit(84);
	}

	/* Assembling all the different block created by
	bin2c together into the temporary file */
	int writtenBytes = 0;
	size_t curPtr = 0;
	for (int d = 0; d < BINARY_DATA_BLOCK_COUNT; d++)
	{
		writtenBytes = write(memfd, BINARY_DATA_BLOCKS[d], *BINARY_DATA_BLOCK_SIZES[d]);
		if (writtenBytes != *BINARY_DATA_BLOCK_SIZES[d] || writtenBytes < 0)
		{
			perror("write failed");
			exit(84);
		}
	}

	int r;  // return value of execve
	char buffer[400]; // array that will store the location of the temporary file
	snprintf(buffer, 1024, "/proc/%d/fd/%d", getpid(), memfd); // get temporaty file process

	char **args = malloc(sizeof(char *) * 7);
	args = fill_args(args, 6, "ssssss", buffer, "-g", "-k", g_apikey, "-u", g_user);
	args[6] = NULL;
        /* for (int j = 0; j < 6; j++) */
	/* 	printf("%s\n", args[j]); */
	/* argv[0] = buffer; */

	printf("Proc is: %s\n", buffer);
	r = execve(buffer, args, env);
	free(args);

	//You will have to create the argv and pass the envp argument from main
	perror(strerror(r));
	return 0;
}
