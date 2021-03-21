#include<stdio.h>

int main(){
	char str[101];
	int len=0;
	scanf("%s%n",str,&len);
	str[len]='*';
	str[len]='\0';
	int count=1;
	for(int i=0;i<len;i++){
		if(str[i]!=str[i+1]){
			printf("%c%d",str[i],count);
			count=1;
			continue;
		}
		count++;
	}
	return 0;
}
