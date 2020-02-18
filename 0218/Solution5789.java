import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution5789 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static int [] fill(int []arr, int l, int r, int input) {
		for(int i = l-1;i<r;i++) {
			arr[i] = input;
		}
		return arr;
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case=1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int Q = Integer.parseInt(st.nextToken());
			int []arr = new int [N];
			for(int i=1;i<=Q;i++) {
				st = new StringTokenizer(br.readLine());
				int L = Integer.parseInt(st.nextToken());
				int R = Integer.parseInt(st.nextToken());
				arr = fill(arr, L, R, i);
			}
			System.out.print("#"+test_case);
			for(int j=0;j<arr.length;j++) System.out.print(" "+arr[j]);
			System.out.println();
		}

	}

}
