
public class Programmers12924 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 15;
		int answer = 0;
		for(int i=1;i<=n;i++) {
			int sum = 0;
			int j = i;
			while(j<=n&&sum<n) {
				sum += j;
				j++;
				if(sum==n) {
					answer++;
					break;
				}
			}
		}
		System.out.println(answer);

	}

}
