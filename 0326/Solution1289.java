import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution1289 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			int result = 0;
			String [] input = br.readLine().split("");
			String tmp = "0";
			for(int i=0;i<input.length;i++) {
				if(tmp.equals(input[i])) {
					
				}
				else {
					tmp = input[i];
					result ++;
				}
			}
			System.out.println("#"+test_case+" "+result);
		}
	}

}
