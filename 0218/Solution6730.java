import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution6730 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case=1;test_case<=T;test_case++) {
			int N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			int [] arr = new int [N];
			int up = 0;
			int down = 0;
			arr[0] = Integer.parseInt(st.nextToken());
			for(int i=1;i<N;i++) {
				arr[i] = Integer.parseInt(st.nextToken());
				if(arr[i-1]<arr[i]) {
					if(arr[i]-arr[i-1]>up)	up = arr[i]-arr[i-1];
				}
				if(arr[i]<arr[i-1]) {
					if(arr[i-1]-arr[i]>down) down = arr[i-1]-arr[i];
				}
			}
			System.out.println("#"+test_case+" "+up+" "+down);
		}
	}

}
