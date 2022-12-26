#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    int largest_sum = 0;
    int second_largest = 0;
    int third_largest = 0;
    int temp_sum = largest_sum;

    fp = fopen("input.txt", "r");
    if (fp == NULL) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    while ((read = getline(&line, &len, fp)) != -1) {
        if (line[0] == '\n') {
            if (temp_sum > largest_sum) {
                third_largest = second_largest;
                second_largest = largest_sum;
                largest_sum = temp_sum;
            } else if (temp_sum > second_largest) {
                third_largest = second_largest;
                second_largest = temp_sum;
            } else if (temp_sum > third_largest) {
                third_largest = temp_sum;
            }
            temp_sum = 0;
        } else {
            temp_sum += atoi(line);
        }
    }

    fclose(fp);
    free(line);
    fprintf(stdout, "Sum: %d\n", largest_sum + second_largest + third_largest);
    return 0;
}