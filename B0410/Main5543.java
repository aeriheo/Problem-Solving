import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main5543 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		int ham = 2001;
		int dri = 2001;
		
		for(int i=0;i<3;i++) {
			int h = Integer.parseInt(br.readLine());
			if(ham>h) ham = h;
		}
		for(int j=0;j<2;j++) {
			int d = Integer.parseInt(br.readLine());
			if(dri>d) dri = d;
		}
		int total = ham + dri - 50;
		System.out.println(total);
	}

}
