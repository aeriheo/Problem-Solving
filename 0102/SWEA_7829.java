import java.util.Scanner;

public class Solution12 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner (System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int P = sc.nextInt();
			int []arr = new int [P];
			int min=1000000;
			int max=0;
			for(int i=0;i<P;i++) {
				arr[i] = sc.nextInt();
				if(max<arr[i]) max = arr[i];
				if(min>arr[i]) min = arr[i];
			}
			int result;
			if(P%2==1) {
				result = arr[P-1] * arr[P-1];
			}else {
				result = min*max;
			}
			System.out.println("#" + test_case + " " + result);
		}
	}

}
