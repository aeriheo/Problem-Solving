
public class ProgrammersPractice6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "pPoooyY";
		boolean answer = true;
		int p = 0, y = 0;
		String [] arr = s.split("");
		for(int i=0;i<arr.length;i++) {
			if(arr[i].equals("p")||arr[i].equals("P")) p++;
			else if (arr[i].equals("y")||arr[i].equals("Y")) y++;
		}
		if(p!=y) answer = false;

	}

}
