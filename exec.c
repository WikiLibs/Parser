
int main(int argc, char **argv, char **env)
{
    int memfd = memfd_create("mybin", MFD_CLOEXEC);
    if (memfd == -1)
	panic("Memfd creation failure");
    size_t curPtr = 0;
    while (curPtr < BINARY_DATA_SIZE)
    {
	write(memfd, &BINARY_DATA[curPtr], 512);
	curPtr += 512;
    }
    fexecve(memfd, argv, envp); //You will have to create the argv and pass the envp argument from main
    return 0;
}
