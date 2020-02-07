import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution8741 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String []arr = new String[st.countTokens()];
			String D;
			for(int i=0;i<arr.length;i++) {
				D = st.nextToken();
				String [] tmp = D.split("");
				arr[i] = tmp[0].toUpperCase();
			}
			System.out.print("#"+test_case+" ");
			for(int j=0;j<arr.length;j++) System.out.print(arr[j]);
			System.out.println();
		}
	}

}
