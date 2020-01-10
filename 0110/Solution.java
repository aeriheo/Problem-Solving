import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

	static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	
	public static void func(String []tk) {
		int a = 0, b = 0, c = 0;
		for(int i=0;i<tk.length;i++) {
			if(tk[i].equals("a")) a++;
			else if(tk[i].equals("b")) b++;
			else c++;
		}
		int ac = a - c;
		if(ac<0) ac *= -1;
		int bc = b - c;
		if(bc<0) bc *= -1;
		int ab = a - b;
		if(ab<0) ab *= -1;
		if(ab<=1&&bc<=1&&ac<=1) System.out.println(" YES");
		else System.out.println(" NO");
	}

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		
		int T = Integer.parseInt(reader.readLine());
		
		for(int test_case = 1;test_case<=T;test_case++) {
			String []s = reader.readLine().split("");
			System.out.print("#"+test_case);
			func(s);
		}

	}

}
