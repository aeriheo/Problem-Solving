import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main10039 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int cnt = 0;
		for(int i=0;i<5;i++) {
			int input = Integer.parseInt(br.readLine());
			if(input<40) input = 40;
			cnt += input;
		}
		int avg = cnt/5;
		System.out.println(avg);
			
	}
}
