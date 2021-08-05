#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* decode(char* ptr)
{
    int length = strlen(ptr);
    unsigned char* buf = (unsigned char*)malloc(length);
    unsigned int xorkey = 0xFF;

    memcpy(buf, ptr, length);
    for (int i = 0; i < length; i++)
    {
        buf[i] ^= xorkey;
    }

    return buf;
}

int main(void)
{
	unsigned char* str = "\xB7\x9A\x93\x93\x90\xDF\xA8\x90\x8D\x93\x9B\xFF";  // "Hello World\x00"

    	printf("%s\n", decode(str));
    
	return 0;
}
