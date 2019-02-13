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

/**
 * Example structure
 */
struct apple {
    /**
     * \brief bool alive 
     * Boolean telling if apple is alive */
    BOOL alive;
    char *serial_no;  /**<Description after */
};

union box {
    apple *food;
};

/**
 * @brief manger function
 * @details function used to eat
 * @param unionVar box containing food
 * @param value random value
 * @return boolean indicating if has eaten
 */
BOOL manger(box unionVar, int value) {
    char p[8] = "crunch\n";
    printf("%s\n", p);
};

#endif