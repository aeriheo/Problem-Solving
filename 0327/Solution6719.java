import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution6719 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			double a = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			double []arr = new double[n];
			for(int i=0;i<n;i++) arr[i] = Double.parseDouble(st.nextToken());
			Arrays.sort(arr);
			for(int j=n-k;j<arr.length;j++) {
				a = (a+arr[j])/2;
			}
			System.out.println("#"+test_case+" "+a);
		}
	}

}
