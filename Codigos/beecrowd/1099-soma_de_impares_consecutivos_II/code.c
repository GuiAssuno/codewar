#include <stdio.h>

int main(){

    int n = 0, x = 0, y = 0, soma = 0;

    for (scanf("%d", &n); n > 0; n--) {
        scanf("%d %d", &x, &y);
        if (x < y){
            for (x = x + 1; x < y; x++){
                if ((x % 2) == 1)
                    soma += x;
            }

        } else {
            for (y = y + 1; y < x; y++){
                if ((y % 2) == 1)
                    soma += y;
            }
        }
        printf("%d\n", soma);
        y = x = soma = 0;
    }

    return 0;
}