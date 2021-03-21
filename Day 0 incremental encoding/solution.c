#include<stdio.h>
int main(){
	char str[101];
	int len;
	scanf("%s%n",str,&len);
	for(int i=0;i<n;i++){
		if(str[i]>='a'&& str[i]<='z'){
			str[i]='a'+(str[i]-'a'+i)%26;}
		}
		else{
			str[i]='A'+(str[i]-'A'+i)%26;}
	printf("%s",str);
	return 0;
}