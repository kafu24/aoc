#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    FILE *fp;
    char *line, *line2, *line3 = NULL;
    char *thing, *thing2 = NULL;
    char firsthalf[256];
    size_t len = 0;
    ssize_t read1, read2, read3, min;
    unsigned long i = 0;
    if ((fp = fopen("input.txt", "r")) == NULL) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }
    // while ((read = getline(&line, &len, fp)) != -1) {
    //     memset(firsthalf, 0, 256);
    //     strncpy(firsthalf, line, read / 2);
    //     if ((thing = strpbrk(line + read / 2, firsthalf)) != NULL) {
    //         i += thing[0] >= 97 ? thing[0] - 96 : thing[0] - 38;
    //     }
    //     fprintf(stdout, "The line read: %s", line);
    //     fprintf(stdout, "The first half: %s\n", firsthalf);
    //     fprintf(stdout, "The second half: %s", line + read / 2);
    //     fprintf(stdout, "The duplicate in both halves: %c\n", *thing);
    // }
    while ((read1 = getline(&line, &len, fp)) != -1 &&
           (read2 = getline(&line2, &len, fp)) != -1 &&
           (read3 = getline(&line3, &len, fp)) != -1) {
        for (int j = 0; j < read1; j++) {
            if ((thing2 = strchr(line2, line[j])) != NULL &&
                (thing = strchr(line3, line[j])) != NULL) {
                printf("Line1: %sLine2: %sLine3: %s", line, line2, line3);
                printf("Character to be found in all three: %c\n", line[j]);
                i += line[j] >= 97 ? line[j] - 96 : line[j] - 38;
                break;
            }
        }
    }
    free(line);
    free(line2);
    free(line3);
    fclose(fp);
    fprintf(stdout, "%ld\n", i);
    return 0;
}