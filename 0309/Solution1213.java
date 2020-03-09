import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution1213 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		for(int test_case = 1;test_case<=10;test_case++) {
			int T = Integer.parseInt(br.readLine());
			String find = br.readLine();
			String real = br.readLine();
			String [] line = real.split(find);
			int cnt = 0;
			for(int i=0;i<line.length;i++) {
				cnt += line[i].length();
			}
			int result = (real.length() - cnt)/find.length();
			System.out.println("#"+test_case+" "+result);
		}
	}

}
