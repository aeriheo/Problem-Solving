
public class ProgrammersPractice14 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long num = 626331;
		int answer = solution(num);
		System.out.println(answer);
	}
	
	public static int solution(long num) {
		int answer = 0;
		while(num!=1&&answer<500) {
			if(num%2==0) {
				num /= 2;
				answer++;
			}else {
				num = (num*3) +1;
				answer++;
			}
		}
		if(answer == 500) answer = -1;
		return answer;
	}

}
