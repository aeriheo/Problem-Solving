import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution3975 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			double alice, bob;
			int a1 = Integer.parseInt(st.nextToken());
			int a2 = Integer.parseInt(st.nextToken());
			int b1 = Integer.parseInt(st.nextToken());
			int b2 = Integer.parseInt(st.nextToken());
			alice = (double)a1/a2;
			bob = (double)b1/b2;
			String result = "";
			if(alice>bob) result = "ALICE";
			else if (alice<bob) result = "BOB";
			else if(alice==bob) result = "DRAW";
			
			System.out.println("#"+test_case+" "+result);
			
		}

	}

}
