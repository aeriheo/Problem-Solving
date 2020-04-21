import java.util.Arrays;

public class ProgrammersPractice3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] array = {1,5,2,6,3,7,4};
		int [][] commands = {{2,5,3},{4,4,1},{1,7,3}};
		int [] answer = new int [commands.length];
		for(int i=0;i<commands.length;i++) {
			int [] tmp = new int [(commands[i][1]-commands[i][0])+1];
			int a = 0;
			int j = commands[i][0]-1;
			while(j<commands[i][1]) {
				tmp[a] = array[j];
				a++;
				j++;
			}
			Arrays.sort(tmp);
			answer[i] = tmp[commands[i][2]-1];
		}
		for(int e : answer) System.out.println(e);
	}

}
