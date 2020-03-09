import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution5603 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			int N = Integer.parseInt(br.readLine());
			int [] s = new int [N];
			int sum = 0;
			for(int i=0;i<N;i++) {
				s[i] = Integer.parseInt(br.readLine());
				sum += s[i];
			}
			int div = sum/N;
			int result = 0;
			for(int j=0;j<N;j++) {
				if(s[j]-div>0) result += s[j]-div;
			}
			System.out.println("#"+test_case+" "+result);
		}
	}

}
