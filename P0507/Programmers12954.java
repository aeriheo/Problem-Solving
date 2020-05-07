
public class Programmers12954 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x =-4;
		int n = 3;
		long [] answer = new long [n];
		long num = (long)x;
		for(int i=0;i<n;i++) {
			answer[i] = num;
			num += (long)x;
		}
		System.out.println(answer[2]);
	}

}
