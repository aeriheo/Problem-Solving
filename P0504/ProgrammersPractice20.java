
public class ProgrammersPractice20 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] arr = {4,3,2,1};
		int [] answer = {};
		int x = arr[0];
		int n = 0;
		if(arr.length!=1) {
			answer = new int [arr.length-1];
			for(int i=1;i<arr.length;i++) {
				if(x>arr[i]) {
					x = arr[i]; 
					n = i;
				}
			}
			int e = 0;
			for(int j=0;j<arr.length;j++) {
				if(j!=n) {
					answer[e] = arr[j];
					e++;
				}
			}
		}else {
			answer = new int [1];
			answer[0] = -1;
		}
	}

}
