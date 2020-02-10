import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution9317 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			int N = Integer.parseInt(br.readLine());
			String [] arr = br.readLine().split("");
			String [] tmp = br.readLine().split("");
			int cnt = 0;
			for(int i = 0;i<N;i++) {
				if(arr[i].equals(tmp[i])) cnt++;
			}
			System.out.println("#"+test_case+" "+cnt);
		}

	}

}
