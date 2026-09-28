#include <stdlib.h>
#include <stdio.h>

int main() {

    int casos = 0, x = 0, y =0;

     while (1) {
        scanf("%d", &casos);
        if (casos == 0) break;
        scanf("%d %d", &x, &y);

        for (int i = 0; i < casos; i++){
            int a, b;
            scanf("%d %d", &a, &b);

            if (a > x && b > y){
                printf("NE\n");
            } else if (a < x && b > y){
                printf("NO\n");
            } else if (a > x && b < y){
                printf("SE\n");
            } else if (a < x && b < y) {
                printf("SO\n");
            } else {
                printf("divisa\n");
            }
        }
    }
    
    return 0;
}