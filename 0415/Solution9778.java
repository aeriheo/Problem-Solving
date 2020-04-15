import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Solution9778 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		HashMap <Integer,Integer> hm = new HashMap<>();
		
		for(int test_case = 1;test_case<=T;test_case++) {
			for(int c = 2;c<12;c++) {
				if(c==10) hm.put(c, 16);
				else hm.put(c,4);
			}
			
			int N = Integer.parseInt(br.readLine());
			int sum = 0;
			
			
			for(int i=0;i<N;i++) {
				int input = Integer.parseInt(br.readLine());
				sum += input;
				int value = hm.get(input);
				hm.put(input,value-1);
				
			}
			String result = "";
			int go = 21 - sum;
			int u = 0, d = 0;
			for(int j=2;j<12;j++) {
				if(j<=go) d+=hm.get(j);
				else u+=hm.get(j);
			}

			if(d<=u) result = "STOP";
			else result = "GAZUA";
			System.out.println("#"+test_case+" "+result);
		}
		

	}

}
