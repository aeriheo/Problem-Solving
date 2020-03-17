import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution7732 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void print(int test_case, int h, int m, int s) {
		System.out.print("#"+test_case+" ");
		if(h<10) {
			System.out.print("0"+h+":");
		}else System.out.print(h+":");
		if(m<10) {
			System.out.print("0"+m+":");
		}else System.out.print(m+":");
		if(s<10) {
			System.out.println("0"+s);
		}else System.out.println(s);
	}
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			String []tmp = br.readLine().split(":");
			int [] arr = new int [tmp.length];
			for(int i=0;i<tmp.length;i++) arr[i] = Integer.parseInt(tmp[i]);
			String []now = br.readLine().split(":");
			int [] ar = new int [now.length];
			for(int i=0;i<now.length;i++) ar[i] = Integer.parseInt(now[i]);
			int h , m, s;
			if(ar[2]<arr[2]) {
				ar[2]+=60;
				s = ar[2] - arr[2];
				ar[1] -= 1;
				if(ar[1]<0) {
					ar[1] = 59;
					ar[0] -= 1;
					if(ar[0]<0) ar[0] = 23;
				}
			}else s = ar[2] - arr[2];
			if(ar[1]<arr[1]) {
				ar[1]+=60;
				m = ar[1] - arr[1];
				ar[0]-=1;
				if(ar[0]<0) ar[0] = 23;
			}else m = ar[1] - arr[1];
			if(ar[0]<arr[0]) {
				ar[0]+=24;
				h = ar[0] - arr[0];
			}else h = ar[0] - arr[0];
			print(test_case, h, m, s);
		}

	}

}
