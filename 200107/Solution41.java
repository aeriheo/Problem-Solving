import java.util.Scanner;

public class Solution41 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int N = sc.nextInt();
			float [] p = new float [N];
			int [] x = new int [N];
			float sum = 0;
			for(int i=0;i<N;i++) {
				p[i] = sc.nextFloat();
				x[i] = sc.nextInt();
				sum += (p[i]*x[i]);
			}
			System.out.println("#" + test_case+" "+sum);
		}
	}

}
