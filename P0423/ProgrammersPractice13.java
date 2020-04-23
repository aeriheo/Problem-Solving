
public class ProgrammersPractice13 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num = 3;
		String answer = solution(num);
		System.out.println(answer);
	}

	public static String solution(int num) {
		String answer = "";
		if(num==0) answer = "Even";
		else if(num%2==0) answer = "Even";
		else answer = "Odd";
		return answer;
	}
}
