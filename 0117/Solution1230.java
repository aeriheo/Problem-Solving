import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution1230 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		ArrayList<Integer> al = new ArrayList<>();
		for(int test_case = 1;test_case<=10;test_case++) {
			int input = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i=0;i<input;i++) {
				al.add(Integer.parseInt(st.nextToken()));
			}
			int order = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<order;j++) {
				int x = 0, y = 0;
				String solv = st.nextToken();
				if(solv.equals("I")) {
					x = Integer.parseInt(st.nextToken());
					y = Integer.parseInt(st.nextToken());
					int m = x;
					for(int cnt = 0;cnt<y;cnt++) {
						al.add(m,Integer.parseInt(st.nextToken()));
						m++;
					}
				}
				else if(solv.equals("D")) {
					x = Integer.parseInt(st.nextToken());
					y = Integer.parseInt(st.nextToken());
					int m = x;
					for(int cnt = 0;cnt<y;cnt++) {
						al.remove(m);
					}
				}
				else if(solv.equals("A")) {
					y = Integer.parseInt(st.nextToken());
					for(int cnt = 0;cnt<y;cnt++) {
						al.add(Integer.parseInt(st.nextToken()));
					}
				}
			}
			System.out.print("#"+test_case);
			for(int e = 0;e<10;e++) System.out.print(" "+al.get(e));
			System.out.println("");
			al.clear();
		}
	}

}
