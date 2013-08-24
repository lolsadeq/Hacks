
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int Main() {

  FILE* fp;
  size_t count;
  const char* str = "Jonas Gorauskas\n";

  fp = fopen("test123.txt", "w");
  if (fp == NULL) {
    perror("File not found!");
    return EXIT_FAILURE;
  }

  count = fwrite(str, 1, strlen(str), fp);
  printf("Wrote %zu bytes. fclose(fp) %s.\n", count, fclose(fp) == 0 ? "succeeded": "failed");
  return EXIT_SUCCESS;
}


