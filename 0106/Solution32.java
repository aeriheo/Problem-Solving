import java.util.Scanner;

public class Solution32 {

	public static int func(int a, int b, int c) {
		int d = 0;
		if(a==b) d = c;
		if(a==c) d = b;
		if(b==c) d = a;
		
		return d;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			int d = func(a,b,c);
			System.out.println("#"+test_case+" "+d);
		}
	}

}
