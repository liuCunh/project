package chapter03;

public class HundredAnimal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int z = 0;
		boolean result = false;
		for(int i = 0; i <= 20; i++){
			for(int j = 0; j <= 33; j++){
				z = 100 - i - j;
				if((z % 3 == 0) && (i*5+j*3+z/3) == 100){
					System.out.println("公鸡="+i+"母鸡="+j+"小鸡="+z);
					result = true;
				}
			}
		}
		if(!result){
			System.out.print("无解");
		}
	}

}
