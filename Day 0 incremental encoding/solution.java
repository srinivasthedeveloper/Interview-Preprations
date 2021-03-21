import java.util.Scanner;
class Solution{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		StringBuffer str=new StringBuffer(sc.next());
		for(int i=0;i<str.length();i++){
			if(str.charAt(i)<='z' && str.charAt(i)>='a'){
				str.setCharAt(i,(char)('a'+(str.charAt(i)-'a'+i)%26));
			}
			else{
				str.setCharAt(i,(char)('A'+(str.charAt(i)-'A'+i)%26));
			}
		}
		System.out.println(str);
	}
}