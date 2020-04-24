import java.util.Arrays;

public class ProgrammersPractice16 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] d = {1,3,2,5,4};
		long budget = 9;
		long tmp = 0;
		int answer = 0;
		Arrays.sort(d);
		for(int i=0;i<d.length;i++) {
			tmp += d[i];
			if(tmp>budget) break;
			answer++;
		}
		System.out.println(answer);

	}

}
