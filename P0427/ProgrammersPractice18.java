
public class ProgrammersPractice18 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 5, b = 24;
		String answer = "";
	      int m = 0;
	      for(int i=1;i<a;i++){
	          if(i==1||i==3||i==5||i==7||i==8||i==10||i==12) m +=31;
	          else if(i==2) m+= 29;
	          else m+=30;
	      }
	      m+=b;
	      int sol = m%7;
	      if(sol==1) answer = "FRI";
	      else if(sol==2) answer = "SAT";
	      else if(sol==3) answer = "SUN";
	      else if(sol==4) answer = "MON";
	      else if(sol==5) answer = "TUE";
	      else if(sol==6) answer = "WED";
	      else answer = "THU";
		System.out.println(answer);
	}

}
