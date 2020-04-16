import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main10817 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws IOException {

		String [] arr = br.readLine().split(" ");
		if(Integer.parseInt(arr[0])>=Integer.parseInt(arr[1])) {
			if(Integer.parseInt(arr[0])<=Integer.parseInt(arr[2])) System.out.println(arr[0]);
			else if(Integer.parseInt(arr[1])>=Integer.parseInt(arr[2])) System.out.println(arr[1]);
			else System.out.println(arr[2]);
		}else if (Integer.parseInt(arr[1])>=Integer.parseInt(arr[2])) {
			if(Integer.parseInt(arr[1])<=Integer.parseInt(arr[0])) System.out.println(arr[1]);
			else if(Integer.parseInt(arr[2])>=Integer.parseInt(arr[0])) System.out.println(arr[2]);
			else System.out.println(arr[0]);
		}else {
			if(Integer.parseInt(arr[2])<=Integer.parseInt(arr[0])) System.out.println(arr[2]);
			else if(Integer.parseInt(arr[1])>=Integer.parseInt(arr[0])) System.out.println(arr[1]);
			else System.out.println(arr[0]);
		}
	}

}
