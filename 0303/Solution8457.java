import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution8457 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static int find(int arr, int b, int e) {
		int result = 0;
		for(int i=1;i<=11440;i++) {
			int mul = arr * i;
			if(mul>=(b-e)) {
				if(mul<=(b+e)) return result+1;
				else if(mul>(b+e)) return result;
			}
		}
		return result;
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			int [] arr = new int [n];
			st = new StringTokenizer(br.readLine());
			for(int i=0;i<n;i++) arr[i] = Integer.parseInt(st.nextToken());
			int result = 0;
			for(int j=0;j<n;j++) {
				result += find(arr[j], b, e);
			}
			System.out.println("#"+test_case+" "+result);
		}
		
	}

}
