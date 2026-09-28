#include <stdio.h>

int main(){

    while(1){
        int senha = 0;
        scanf("%d", &senha);
        if (senha == 2002) break;    
        printf("Senha Invalida\n");        
    }

    printf("Acesso Permitido\n");
    return 0;
}
     