import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main4344 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int sum = 0;
			int [] arr = new int [N];
			for(int i=0;i<N;i++) {
				arr[i] = Integer.parseInt(st.nextToken());
				sum += arr[i];
			}
			double avg = (double)sum/N;
			int cnt = 0;
			for(int j=0;j<N;j++) {
				if(arr[j]>avg) cnt++;
			}
			double stu = ((double)cnt/N )* 100;
			System.out.println(String.format("%.3f", stu)+"%");
		}

	}

}
