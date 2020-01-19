import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Solution8821 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		int T = Integer.parseInt(br.readLine());
		for(int test_case = 1;test_case<=T;test_case++) {
			ArrayList<String> al = new ArrayList<>();
			String [] arr = br.readLine().split("");
			for(int i=0;i<arr.length;i++) {
				if(al.isEmpty()) al.add(arr[i]);
				else if(al.contains(arr[i])) al.remove(arr[i]);
				else al.add(arr[i]);
			}
			System.out.println("#"+test_case+" "+al.size());
		}
	}

}
