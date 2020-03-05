import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution5162 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void func(int a, int b, int c, int test_case) {
		int result = 0;
		int n;
		if(a<b) {
			result = c/a;
			n = c%a;
			if(b<=n) result = result + (n/b);
		}else {
			result = c/b;
			n = c%b;
			if(a<=n) result = result + (n/a);
		}
		System.out.println("#"+test_case+" "+result);
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			func(A, B, C, test_case);
		}

	}

}
