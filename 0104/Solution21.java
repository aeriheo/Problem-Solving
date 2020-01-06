import java.util.Scanner;
import java.util.Stack;

public class Solution21 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack<Integer> stack = new Stack<>();
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int k = sc.nextInt();
			int sum = 0;
			for(int i=0;i<k;i++) {
				int n = sc.nextInt();
				if(n!=0) stack.add(n);
				else stack.pop();
			}
			int m = stack.size();
			for(int i=1;i<=m;i++) {
				sum += stack.pop();
			}
			System.out.println("#"+test_case+" "+sum);
		}
	}

}
