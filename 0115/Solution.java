import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String [] arr = (st.nextToken()).split("");
			int result = 0;
			int cnt = 0;
			for(int i=0;i<arr.length/2;i++) {
				if(arr[i].equals(arr[arr.length-(i+1)])) cnt ++;
			}
			if(cnt==arr.length/2) result = 1;
			System.out.println("#"+test_case+" "+result);
		}
	}

}
