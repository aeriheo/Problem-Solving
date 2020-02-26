import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution4466 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			int [] arr = new int [N];
			st = new StringTokenizer(br.readLine());
			for(int i=0;i<N;i++) arr[i] = Integer.parseInt(st.nextToken());
			Arrays.sort(arr);
			int sum = 0;
			int j = arr.length-1;
			int cnt = 0;
			while(cnt<K) {
				sum += arr[j];
				j--;
				cnt++;
			}
			System.out.println("#"+test_case+" "+sum);
		}

	}

}
