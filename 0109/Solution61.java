import java.util.Scanner;

public class Solution61 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner (System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int N = sc.nextInt();
			int D = sc.nextInt();
			int [] arr = new int [N];
			int cnt = 0;
			int result = 0;
			for(int i=0;i<N;i++) {
				arr[i] = sc.nextInt();
				if(arr[i]==0) {
					cnt++;
					if(cnt==D) {
						cnt = 0;
						result++;
					}
				}
				else cnt = 0;
			}
			System.out.println("#"+test_case+" "+result);
		}

	}

}
