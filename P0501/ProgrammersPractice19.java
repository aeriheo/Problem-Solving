import java.util.Arrays;

public class ProgrammersPractice19 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long n = 118372;
		long answer = 0;
		String a = Long.toString(n);
		String [] arr = a.split("");
		Arrays.sort(arr);
		String b = "";
		for(int i=arr.length-1;i>=0;i--) b += arr[i];
		answer = Long.parseLong(b);
		System.out.println(answer);

	}

}
