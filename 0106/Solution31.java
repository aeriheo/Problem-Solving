import java.util.Scanner;

public class Solution31 {
		
	public static int func(String s) {
		int sum=0;
		String [] str = s.split("");
		int [] itg = new int [str.length];
		for(int m=0;m<str.length;m++) {
			itg[m] = Integer.parseInt(str[m]);
			sum+=itg[m];
		}
		return sum;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		String [] arr = new String [10];
		for(int test_case = 1;test_case<=T;test_case++) {
			int max = 0;
			int min = 55;
			for(int i=0;i<10;i++){
				int temp = sc.nextInt();
				arr[i] = Integer.toString(temp);
				int sum = func(arr[i]);
				if(max<sum) max = sum;
				if(min>sum) min = sum;
			}
			System.out.println("#"+test_case+" "+max+" "+min);
		}
	}

}
