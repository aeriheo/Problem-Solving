import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution1206 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		for(int test_case = 1;test_case<=10;test_case++) {
			int len = Integer.parseInt(br.readLine());
			int [] arr = new int [len];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i=0;i<len;i++) arr[i] = Integer.parseInt(st.nextToken());
			int cnt = 0;
			for(int j=2;j<len-2;j++) {
				int tmp = 0;
				int tcnt = 0;
				if((arr[j]-arr[j-1])>=0) {
					tcnt++;
					tmp = arr[j]-arr[j-1];
				}
				if((arr[j]-arr[j-2])>=0) {
					tcnt++;
					if((arr[j]-arr[j-2])<=tmp) tmp = arr[j]-arr[j-2];
				}
				if((arr[j]-arr[j+1])>=0) {
					tcnt++;
					if((arr[j]-arr[j+1])<=tmp) tmp = arr[j]-arr[j+1];
				}
				if((arr[j]-arr[j+2])>=0) {
					tcnt++;
					if((arr[j]-arr[j+2])<=tmp) tmp = arr[j]-arr[j+2];
				}
				if(tcnt==4) cnt+=tmp;
			}
			System.out.println("#"+test_case+" "+cnt);
		}

	}

}
