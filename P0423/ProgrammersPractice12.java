
public class ProgrammersPractice12 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 11;
		boolean answer = solution(x);
		System.out.println(answer);
	}
	
	public static boolean solution(int x) {
		boolean answer = true;
		String s = Integer.toString(x);
		String [] tmp = s.split("");
		int sum = 0;
		for(int i=0;i<tmp.length;i++) sum += Integer.parseInt(tmp[i]);
		if(x%sum==0) answer = true;
		else answer = false;
		return answer;
	}

}
