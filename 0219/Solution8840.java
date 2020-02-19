import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution8840 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void find(long L, int test_case) {
		long value = L/2;
		System.out.println("#"+test_case+" "+(value*value));
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseUnsignedInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			long L = Long.parseLong(br.readLine());
			find(L, test_case);
		}
	}

}
