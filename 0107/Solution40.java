import java.util.Scanner;

public class Solution40 {

	public static int func(int b, int []a) { //B가 투표한 A찾기
		int cnt = -1;
		for(int i=0;i<a.length;i++) {
			if(a[i]<=b) {
				cnt = i;
				return cnt;
			}
		}
		return cnt;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int []A = new int [N];
			int []B = new int [M];
			int []C = new int [N]; //투표값 저장
			for(int i=0;i<N;i++) {
				A[i] = sc.nextInt();
				C[i] = 0;
			}
			for(int j=0;j<M;j++) {
				B[j] = sc.nextInt();
				int m = func(B[j],A);
				C[m]++;
			}
			int max = 0; //최대 득표 값
			int s =-1; //최대 득표한 번호
			for(int q=0;q<N;q++) {
				if(C[q]>max) {
					max=C[q];
					s=q;
				}
			}
			s++;
			System.out.println("#"+test_case+" "+s);
		}

	}

}
