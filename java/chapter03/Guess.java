package chapter03;

public class Guess {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("----------��Ϸ��ʼ��-----------");
		int computerTotal = 0; 
		int myTotal = 0;
		int i = 1;
		while(computerTotal <= 2 || myTotal <= 2){
			System.out.print("------��ʼ������------");
			System.out.println("��"+i+"��");
			int computerNum = (int)Math.floor((Math.random()*100 + 1) / 16);
			System.out.println("�������ӵ�����"+computerNum);
			int myNum = (int)Math.floor((Math.random()*100 + 1) / 16);
			System.out.println("������ӵ�����"+myNum);
			
			if(computerNum == myNum){
				System.out.println("ƽ�֣�");
			}
			else if(computerNum > myNum){
				computerTotal++;
			}
			else{
				myTotal++;
			}
			
			
			if(computerTotal == 2){
				System.out.println("=========�ȴ���Ϣ���ս��=========");
				System.out.println("���ź���������˵���");
				break;
			}
			else if(myTotal == 2){
				System.out.println("=========�ȴ���Ϣ���ս��=========");
				System.out.println("��ϲ�㣬��Ӯ�ˣ�");
				break;
			}
			i++;
		}
		System.out.println("----------��Ϸ������-----------");
	}

}
