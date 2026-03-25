#include "args_parser.hpp"
#include <cstdlib>

int main() {
    ArgsParser a;
    return a.Help() ? EXIT_FAILURE:EXIT_SUCCESS;
}