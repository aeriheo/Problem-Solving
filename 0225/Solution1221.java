import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution1221 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static int ch_string(String ch) {
		int num = 0;
		switch(ch) {
		case "ZRO" : num = 0; break;
		case "ONE" : num = 1; break;
		case "TWO" : num = 2; break;
		case "THR" : num = 3; break;
		case "FOR" : num = 4; break;
		case "FIV" : num = 5; break;
		case "SIX" : num = 6; break;
		case "SVN" : num = 7; break;
		case "EGT" : num = 8; break;
		case "NIN" : num = 9; break;
		}
		return num;
	}
	
	public static String ch_int (int ch) {
		String num = "";
		switch(ch) {
		case 0 : num = "ZRO"; break;
		case 1 : num = "ONE"; break;
		case 2 : num = "TWO"; break;
		case 3 : num = "THR"; break;
		case 4 : num = "FOR"; break;
		case 5 : num = "FIV"; break;
		case 6 : num = "SIX"; break;
		case 7 : num = "SVN"; break;
		case 8 : num = "EGT"; break;
		case 9 : num = "NIN"; break;
		}
		return num;
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String te = st.nextToken();
			int len = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			int [] arr = new int [len];
			String [] real = new String [len];
			for(int i=0;i<len;i++) {
				real[i] = st.nextToken();
				arr[i] = ch_string(real[i]);
			}
			Arrays.sort(arr);
			System.out.println("#"+test_case);
			for(int j=0;j<len;j++) {
				real[j] = ch_int(arr[j]);
				System.out.print(real[j]+" ");
			}
			System.out.println();
		}
	}

}
