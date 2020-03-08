import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Solution3260 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			BigInteger bi = new BigInteger("0");
			bi = bi.add(new BigInteger(st.nextToken()));
			bi = bi.add(new BigInteger(st.nextToken()));
			
			System.out.println("#"+test_case+" "+bi);
		}

	}

}
