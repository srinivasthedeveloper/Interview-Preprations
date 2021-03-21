import java.util.Scanner;
class RunLengthEncoding{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		String str=sc.next()+"*";
		int count=0;
		for(int i=0;i<str.length()-1;i++){
			count++;
			if(str.charAt(i)!=str.charAt(i+1)){
				System.out.print(str.charAt(i)+""+count);
				count=0;
			}
		}
	}
}