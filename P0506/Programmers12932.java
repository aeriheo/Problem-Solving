
public class Programmers12932 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long n = 12345;
		String s = Long.toString(n);
		int [] answer = new int [s.length()];
		String [] ss = s.split("");
		int e = 0;
		for(int i=ss.length-1;i>=0;i--) {
			answer[e] = Integer.parseInt(ss[i]);
			e++;
		}
	}

}
