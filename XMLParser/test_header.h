#ifndef TEST_HEADER_
# define TEST_HEADER_

#include <stdio.h>

#define TRUE 1
#define FALSE 0
#define IS_POSITIVE(t) (t >= 0)
/**
 * Sums the given numbers
 */
#define SUM(x, y) (x + y)

typedef int BOOL;

struct apple {
    BOOL alive;
    char *serial_no;
};

union box {
    apple *food;
};

BOOL manger(box) {
    char p[8] = "crunch\n";
    printf("%s\n", p);
};

#endif