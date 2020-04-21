
public class ProgrammersPractice7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String []seoul = {"Jane","Kim"};
		String answer = "김서방은 ";
		int l = 0;
		for(int i=0;i<seoul.length;i++) {
			if(seoul[i].equals("Kim")) l = i;
		}
		answer += Integer.toString(l);
		answer += "에 있다";
	}

}
