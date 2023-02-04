package chapter03;

public class Nest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 0, y = 0;
		if (x == 1) {
			if (y == 1) 
				System.out.print("x=1, y=1");
			else 
				System.out.print("x=1, y!=1");
		}else {
			if (y==1)
				System.out.println("x!=1, y=1");
			else
				System.out.println("x!=1, y!=1");
		}
	}

}
