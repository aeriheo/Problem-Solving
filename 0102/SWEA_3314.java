import java.util.Scanner;

public class Solution11 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int [] arr = new int [5];
			int sum = 0;
			for(int i=0;i<5;i++) {
				arr[i]=sc.nextInt();
				if (arr[i]<40) arr[i]=40;
				sum += arr[i];
			}
			int result = sum/5;
			System.out.println("#" + test_case + " " + result);
			
		}
	}

}
