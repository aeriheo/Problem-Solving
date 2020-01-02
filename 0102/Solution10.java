import java.util.Scanner;

public class Solution10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int L = sc.nextInt();
			int U = sc.nextInt();
			int X = sc.nextInt();
			int result;
			if(X<L) result = L-X;
			else if(X>U) result = -1;
			else result = 0;
			
			System.out.println("#" + test_case + " " + result);
		}
	}

}
