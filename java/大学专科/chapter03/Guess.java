package chapter03;

public class Guess {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("----------游戏开始啦-----------");
		int computerTotal = 0; 
		int myTotal = 0;
		int i = 1;
		while(computerTotal <= 2 || myTotal <= 2){
			System.out.print("------开始扔骰子------");
			System.out.println("第"+i+"局");
			int computerNum = (int)Math.floor((Math.random()*100 + 1) / 16);
			System.out.println("电脑骰子点数："+computerNum);
			int myNum = (int)Math.floor((Math.random()*100 + 1) / 16);
			System.out.println("你的骰子点数："+myNum);
			
			if(computerNum == myNum){
				System.out.println("平局！");
			}
			else if(computerNum > myNum){
				computerTotal++;
			}
			else{
				myTotal++;
			}
			
			
			if(computerTotal == 2){
				System.out.println("=========等待休息最终结果=========");
				System.out.println("很遗憾，你输给了电脑");
				break;
			}
			else if(myTotal == 2){
				System.out.println("=========等待休息最终结果=========");
				System.out.println("恭喜你，你赢了！");
				break;
			}
			i++;
		}
		System.out.println("----------游戏结束啦-----------");
	}

}
