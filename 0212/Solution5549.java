import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution5549 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			String [] arr = br.readLine().split("");
			int tmp = Integer.parseInt(arr[arr.length-1]);
			String result = null;
			if(tmp%2==0) result = "Even";
			else if(tmp%2==1) result = "Odd";
			System.out.println("#"+test_case+" "+result);
		}
	}

}
