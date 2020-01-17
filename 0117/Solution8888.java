import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution8888 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void func (int test_case) throws IOException{
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int T = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());
		int [][] arr = new int [N][T+2];
		for(int i=0;i<N;i++) {
			int cnt = 0;
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<T;j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if(arr[i][j]==1) cnt++;
			}
			arr[i][T+1] = cnt; //풀이한 문제수
		}
		int [] solv = new int [T];
		for(int n = 0;n<T;n++) {
			int cnt2 = 0;
			for(int s = 0;s<N;s++) {
				if(arr[s][n]==0) cnt2++;
			}
			solv[n] = cnt2;
		}
		for(int w = 0;w<N;w++) {
			int point = 0;
			for(int u = 0;u<T;u++) {
				if(arr[w][u]==1) point=point+(1*solv[u]);
			}
			arr[w][T] = point;
		}
		int up = 0;
		for(int m = 0;m<N;m++) {
			if(arr[P-1][T]<arr[m][T]) up++;
			else if(arr[P-1][T]==arr[m][T]) {
				if(arr[P-1][T+1]<arr[m][T+1]) up++;
				else if(arr[P-1][T+1]==arr[m][T+1]&&m<P-1) up++;
			}
		}
		System.out.println("#"+test_case+" "+arr[P-1][T]+" "+(up+1));
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		int Tc = Integer.parseInt(br.readLine()); //test case
		for(int test_case = 1;test_case<=Tc;test_case++) {
			func(test_case);
		}
	}
	
}
