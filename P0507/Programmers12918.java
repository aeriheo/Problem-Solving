public class Programmers12918 {

	public static void main(String[] args) {
		String s = "123456";
		boolean answer = true;
		if(s.length()==4||s.length()==6) {
			for(char c : s.toCharArray()) { //숫자판별
				if(c<48 || c>57) {
					answer = false;
					break;
				}
			}
		}
		else answer = false;
		System.out.println(answer);
	}

}
