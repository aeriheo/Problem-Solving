import java.util.Scanner;

public class Solution30 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int p = sc.nextInt();
			System.out.print("#"+test_case);
			for(int i=0;i<p;i++) {
				System.out.print(" 1/"+p);
			}
			System.out.println( );
		}
	}

}
