import java.util.ArrayList;

public class ProgrammersPractice4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int []arr = {1,1,3,3,0,1,1};
		ArrayList <Integer> al = new ArrayList<>();
		al.add(arr[0]);
		int s = 0;
		for(int i=1;i<arr.length;i++) {
			if(al.get(s)!=arr[i]) {
				s++;
				al.add(arr[i]);
			}
		}
		int [] answer = new int [al.size()];
		for(int j = 0 ;j<al.size();j++) answer[j] = al.get(j);
		
	}
}
