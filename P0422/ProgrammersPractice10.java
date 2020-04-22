
public class ProgrammersPractice10 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String phone_number = "01033334444";
		String [] tmp = phone_number.split("");
		String answer = "";
		for(int i=0;i<tmp.length;i++) {
			if(i<(tmp.length-4)) answer += "*";
			else answer += tmp[i];
		}
		System.out.println(answer);
	}

}
