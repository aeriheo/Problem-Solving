import java.util.Scanner;

public class Solution20 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case<=T;test_case++) {
			long data = sc.nextInt();
			long s1 = 0 , s2 = 0, s3 = 0;
			s1 = (data*(data+1))/2;
			s3 = s1 * 2;
			s2 = s3 - data;
			System.out.println("#"+test_case+" "+s1+ " "+s2+" "+s3);
		}
	}

}
