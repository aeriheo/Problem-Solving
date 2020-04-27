
public class ProgrammersPractice17 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long n = 987;
		String s = Long.toString(n);
		String [] arr = s.split("");
		int answer = 0;
		for(int i=0;i<arr.length;i++) answer += Integer.parseInt(arr[i]);
		System.out.println(answer);
		

	}

}
