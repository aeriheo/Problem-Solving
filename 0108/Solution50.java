import java.util.Scanner;

public class Solution50 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1;test_case<=T;test_case++) {
			int D = sc.nextInt();
			int H = sc.nextInt();
			int M = sc.nextInt();
			int result = 0;
			if(D==11&&H==11&&M==11) result = 0; //일치할 경우
			else if(D==11&&H==11&&M<11) result = -1;
			else if(D==11&&H<11) result = -1;
			else if(D==11&&H<11&&M<11) result = -1;
			else if(D>=11) {
				int dd = 0, hh = 0, mm = 0;
				if(H>=11) {
					if(M>=11) {
						dd = (D-11) * 1440;
						hh = (H-11) * 60;
						mm = M - 11;
					}
					else { // M<11
						mm = 60 - (11 - M);
					}
				}
				else { // H<11
					if(M>=11) {
						dd = (D-12) * 1440;
						hh = (24 - (11 - H)) * 60;
						mm = M - 11;
					}
					else { // M<11
						mm = 60 - (11 - M);
						hh = (24 - (12 - H)) * 60;
						dd = (D-12) * 1440;
					}
					
				}
				result = dd + hh + mm;
				
			}
			System.out.println("#" + test_case + " " +result);
		}
	}

}
