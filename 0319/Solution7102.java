import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution7102 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			int min, cnt;
			if(n<=m) {
				min = n;
				cnt = m-n;
			}
			else {
				min = m;
				cnt = n-m;
			}
			int many = 1+min;
			System.out.print("#"+test_case);
			for(int i=0;i<=cnt;i++) {
				System.out.print(" "+many);
				many++;
			}
			System.out.println();
		}
	}

}
