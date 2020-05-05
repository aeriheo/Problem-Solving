
public class ProgrammersPractice21 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "3people unFollowed me ";
		String answer = "";
		int len = s.length();
		String []tmp = s.split(" ");
		for(int i=0;i<tmp.length;i++) {
			String [] e = tmp[i].split("");
			e[0] = e[0].toUpperCase();
			answer += e[0];
			for(int j=1;j<e.length;j++) {
				e[j] = e[j].toLowerCase();
				answer += e[j];
			}
			if(i!=tmp.length-1) answer += " ";
			else if(answer.length()==len-1) answer += " ";
		}
		System.out.println(answer);
	}

}
