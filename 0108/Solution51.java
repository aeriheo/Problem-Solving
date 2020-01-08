import java.util.Scanner;

public class Solution51 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner (System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int N = sc.nextInt();
			int K = sc.nextInt();
			int [] arrN = new int [N];
			int [] arrK = new int [N-K];
			for(int i=0;i<N;i++) {
				arrN[i] = i+1;
			}
			for(int j=0;j<K;j++) {
				int NK = sc.nextInt();
				arrN[NK-1] = 0;
			}
			int m = 0;
			for(int s = 0;s<N;s++) {
				if(arrN[s]!=0) {
					arrK[m] = arrN[s];
					m++;
				}
			}
			System.out.print("#"+test_case);
			for(int p=0;p<arrK.length;p++) System.out.print(" "+arrK[p]);
			System.out.println("");
		}

	}

}
