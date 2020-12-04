#include <stdlib.h>

#ifdef __cplusplus
extern "C"
{
#endif

extern const size_t BINARY_DATA_1_SIZE;
extern const unsigned char BINARY_DATA_1[];

static const unsigned char *BINARY_DATA_BLOCKS[] = {
	BINARY_DATA_1
};

static const size_t *BINARY_DATA_BLOCK_SIZES[] = {
	&BINARY_DATA_1_SIZE
};

#ifdef __cplusplus
}
#endif
#define BINARY_DATA_SIZE 50176
#define BINARY_DATA_BLOCK_COUNT 1
