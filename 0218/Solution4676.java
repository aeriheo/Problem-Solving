import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution4676 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case=1;test_case<=T;test_case++) {
			String [] arr = br.readLine().split("");
			int H = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i=0;i<H;i++) {
				int find = Integer.parseInt(st.nextToken());
				if(find==0) {
					String tmp = arr[0];
					arr[0] = "-"+tmp;
				}else{
					arr[find-1] +="-";
				}
			}
			System.out.print("#"+test_case+" ");
			for(int j=0;j<arr.length;j++) System.out.print(arr[j]);
			System.out.println();
		}
	}

}
