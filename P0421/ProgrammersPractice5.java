import java.util.ArrayList;
import java.util.Arrays;

public class ProgrammersPractice5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList <Integer> al = new ArrayList<>();
		int [] arr = {5,9,7,10};
		Arrays.sort(arr);
		int divisor = 5;
		for(int i=0;i<arr.length;i++) {
			if(arr[i]%divisor==0) al.add(arr[i]);
		}
		if(al.size()==0) al.add(-1);
		int [] answer = new int [al.size()];
		for(int j=0;j<al.size();j++) answer[j] = al.get(j);
	}

}
