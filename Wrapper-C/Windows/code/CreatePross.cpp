#include <windows.h>
#include <iostream>
#include <string>
#include <array>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <tchar.h>
#include <strsafe.h>
#include "mybin.h"
#include "constant.h"

int _tmain(int argc, TCHAR* argv[])
{
    STARTUPINFOA si;
    PROCESS_INFORMATION pi;
    LPCSTR binName = "mybin.exe";

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));


    //_tprintf(_T("%s\n"), argv[1]);
    /*for (int i = 0; i < argc; i++) 
    {
        _tprintf(_T("%d = %s\n"), i, argv[i]);
    }*/

    //std::wstring cmdLine = argv[1];
    
    //cmdLine = cmdLine.substr(cmdLine.rfind('\\') + 1, cmdLine.length() - cmdLine.rfind('\\') - 1);
    //_tprintf(_T("cmd line is: %s\n"), cmdLine.c_str());

    if (argc != 2)
    {
        _tprintf(_T("Usage: %s [cmdline]\n"), argv[0]);
        return 1;
    }

    if (BINARY_DATA_SIZE == 0)
    {
        _tprintf(_T("No Blocks\n"));
        return 1;
    }
    /*std::wstring args = argv[1];
    cmdLine.push_back(_T(' '));
    cmdLine.append(args);
    _tprintf(_T("%s\n"), cmdLine.c_str());*/

    // CreateFileA, CloseHandle, WriteFile, DeleteFileA
    HANDLE hFile;
    /*std::array<char, BINARY_DATA_SIZE>(BINARY_DATA);
    std::string[BINARY_DATA_SIZE] = BINARY_DATA;
    LPCWSTR test = std::wstring[](BINARY_DATA);*/
    const char DataBuffer[] = "This is some test data to write to the file.";
    DWORD dwTotalBytesToWrite = BINARY_DATA_SIZE;
    DWORD dwBytesToWrite = 0;
    DWORD dwBytesWritten = 0;
    BOOL bErrorFlag = FALSE;

    // ******** CreateFileA ********
    hFile = CreateFileA(
        binName,             // name of the writess
        GENERIC_WRITE,          // open for writing
        0,                      // do not share
        NULL,                   // default security
        CREATE_NEW,             // create new file only
        FILE_ATTRIBUTE_NORMAL,  // normal file
        NULL);                  // no attr. template
    // ******** !CreateFileA ********

    // ******** CreateFileA Error ********
    if (hFile == INVALID_HANDLE_VALUE)
    {
        printf("Terminal failure: Unable to open file \"%s\" for write.\n", binName);
        return 1;
    }
    // ******** !CreateFileA Error ********

    // ******** WriteFile ********
    //bErrorFlag = WriteFile(
    //    hFile,           // open file handle
    //    DataBuffer,      // start of data to write
    //    dwBytesToWrite,  // number of bytes to write
    //    &dwBytesWritten, // number of bytes that were written
    //    NULL);            // no overlapped structure

    for (DWORD count = 0; count < BINARY_DATA_BLOCK_COUNT; count++)
    {
        dwBytesToWrite = (DWORD)*BINARY_DATA_BLOCK_SIZES[count];
        bErrorFlag = WriteFile(
            hFile,           // open file handle
            BINARY_DATA_BLOCKS[count],     // start of data to write
            dwBytesToWrite,  // number of bytes to write
            &dwBytesWritten, // number of bytes that were written
            NULL);            // no overlapped structure

        // ******** WriteFile Error ********
        if (FALSE == bErrorFlag)
        {
            printf("Terminal failure: Unable to write to file.\n");
        }
        else
        {
            if (dwBytesWritten != dwBytesToWrite)
            {
                // This is an error because a synchronous write that results in
                // success (WriteFile returns TRUE) should write all data as
                // requested. This would not necessarily be the case for
                // asynchronous writes.
                printf("Warning: dwBytesWritten != dwBytesToWrite\n");
            }
            else
            {
                _tprintf(TEXT("Wrote %d bytes to %s successfully.\n"), dwBytesWritten, argv[1]);
            }
        }
        // ******** !WriteFile Error ********
    }
    // ******** !WriteFile ********


    CloseHandle(hFile);

    // ******** CreateProcessA ********
    //std::string ccmdLine(cmdLine.begin(), cmdLine.end());
    //LPSTR lpCmdLine = _strdup(ccmdLine.c_str());
    //printf("lpcmdLine is: #%s#\n", lpCmdLine);
    std::string cmd = binName;
    cmd += _strdup(" -g");
    cmd += _strdup(" -k ");
    cmd += _strdup(g_apikey);
    cmd += _strdup(" -u ");
    cmd += _strdup(g_user);
    LPSTR lpcmdLine = _strdup(cmd.c_str());
    //std::cout << cmd << std::endl;
    for (int i = 0; i < 6; i++)
        if (lpcmdLine[i] == NULL)
            return 1;
    printf("lpcmdLine is: #%s#\n", lpcmdLine);


    if (!CreateProcessA(
        NULL,           // No module name (use command line)
        lpcmdLine,      // Command line
        NULL,           // Process handle not inheritable
        NULL,           // Thread handle not inheritable
        FALSE,          // Set handle inheritance to FALSE
        0,              // No creation flags
        NULL,           // Use parent's environment block
        NULL,           // Use parent's starting directory
        &si,            // Pointer to STARTUPINFO structure
        &pi)            // Pointer to PROCESS_INFORMATION structure
        )
    {
        printf("CreateProcessA failed (%d).\n", GetLastError());
        return 1;
    }
    // ******** !CreateProcessA ********

    // Wait until child process exits.
    WaitForSingleObject(pi.hProcess, INFINITE);

    // Close process, Delete file and thread handles.
    DeleteFileA(binName);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    return 0;
}