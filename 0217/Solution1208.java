import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution1208 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static int[] find(int [] arr) {
		int max = 0;
		int min = 101;
		int maxnum = -1;
		int minnum = -1;
		for(int i=0;i<100;i++) {
			if(arr[i]>max) {
				max = arr[i];
				maxnum = i;
			}
			if(arr[i]<min) {
				min = arr[i];
				minnum = i;
			}
		}
		arr[maxnum]--;
		arr[minnum]++;
		return arr;
	}
	
	public static void minus(int [] arr, int test_case) {
		int max = 0;
		int min = 101;
		for(int i=0;i<100;i++) {
			if(arr[i]>max) {
				max = arr[i];
			}
			if(arr[i]<min) {
				min = arr[i];
			}
		}
		System.out.println("#"+test_case+" "+(max-min));
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		for(int test_case = 1;test_case <= 10;test_case++) {
			int dump = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			String [] tmp = new String [100];
			int [] arr = new int [100];
			for(int i=0;i<100;i++) {
				tmp[i] = st.nextToken();
				arr[i] = Integer.parseInt(tmp[i]);
			}
			for(int j = 1; j <= dump ; j++) {
				arr = find(arr);
			}
			minus(arr, test_case);
		}
	}

}
