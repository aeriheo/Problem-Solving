import java.util.Scanner;

public class Solution60 {
	public static void func(int i, int n, int k) {
		int sum = i;
		int s = sum;
		for(int j = 1; j<n;j++) {
			if(j%2==1) {
				s = s + ((2*k)-(2*i)+1);
				
			}else {
				s = s + ((2*i)-1);
				
			}
			sum+=s;
		}
		System.out.print(" "+sum);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner (System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case <= T; test_case++) {
			int N = sc.nextInt(); //1조당 몇 명?
			int K = sc.nextInt(); //총 몇 조?
			System.out.print("#"+test_case);
			for(int i=1;i<=K;i++) {
				func(i, N, K);
			}
			
			System.out.println("");
		}

	}

}
