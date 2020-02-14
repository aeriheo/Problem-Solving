import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution3499 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void fun1(int cnt, int test_case) throws IOException {
		StringTokenizer st = new StringTokenizer(br.readLine());
		String []tmp1 = new String[cnt/2];
		String [] tmp2 = new String[cnt/2];
		for(int i=0;i<(cnt/2);i++) {
			tmp1[i] = st.nextToken();
		}
		for(int j=0;j<(cnt/2);j++) {
			tmp2[j] = st.nextToken();
		}
		System.out.print("#"+test_case);
		for(int m=0;m<(cnt/2);m++) {
			System.out.print(" "+tmp1[m]+" "+tmp2[m]);
		}
		System.out.println();
	}
	
	public static void func2(int cnt, int test_case) throws IOException {
		StringTokenizer st = new StringTokenizer(br.readLine());
		String []tmp1 = new String[(cnt+1)/2];
		String [] tmp2 = new String[(cnt-1)/2];
		for(int i=0;i<((cnt+1)/2);i++) {
			tmp1[i] = st.nextToken();
		}
		for(int j=0;j<((cnt-1)/2);j++) {
			tmp2[j] = st.nextToken();
		}
		System.out.print("#"+test_case);
		for(int m=0;m<((cnt-1)/2);m++) {
			System.out.print(" "+tmp1[m]+" "+tmp2[m]);
		}
		System.out.println(" "+tmp1[tmp1.length-1]);
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case=1;test_case<=T;test_case++) {
			int cnt = Integer.parseInt(br.readLine());
			if(cnt%2==0) fun1(cnt, test_case);
			else func2(cnt, test_case);
		}

	}

}
