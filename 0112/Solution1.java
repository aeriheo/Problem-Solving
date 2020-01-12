import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution1 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void func(String s) {
		if(s.equals("a")) {
			
		}
		else if (s.equals("e")) {
			
		}
		else if (s.equals("i")) {
			
		}
		else if (s.equals("o")) {
			
		}else if (s.equals("u")) {
			
		}else System.out.print(s);
	}
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			String [] str = br.readLine().split("");
			System.out.print("#"+test_case+" ");
			for(int i=0;i<str.length;i++) {
				func(str[i]);
			}
			System.out.println("");
		}
	}
}
