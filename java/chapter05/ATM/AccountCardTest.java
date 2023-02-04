package chapter05.ATM;

import java.util.Scanner;

public class AccountCardTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AccountCard.setInterest(0.03);  // 年利率
		System.out.println("年利率："+AccountCard.getInterest());
		String account, name, id, address;
		double balance;
		Scanner input = new Scanner(System.in);
		System.out.println("请输入账号：");
		account = input.next();
		System.out.println("请输入姓名：");
		name = input.next();
		System.out.println("请输入身份证号：");
		id = input.next();
		System.out.println("请输入地址：");
		address = input.next();
		System.out.println("请输入金额：");
		balance = input.nextDouble();
		
		AccountCard wang = new AccountCard(account, name, id, address, balance);
		// 构造方法初始化持卡人信息
//		AccountCard wang = new AccountCard();
		int choice; double cash;
		do {
			wang.menu();  // 输入数字，选择菜单
			choice = input.nextInt();
			switch(choice) {
			case 1:  // 存款
				cash = input.nextDouble();
				wang.deposit(cash);
				break;
			case 2:  // 取款
				cash = input.nextDouble();
				wang.withdraw(cash);
				break;
			case 3:  // 购物
				cash = input.nextDouble();
				wang.purchase(cash);
				break;
			case 4:  // 查询
				wang.query();  
				break;
			case 5:
				System.out.println("谢谢你的使用！");
				System.exit(1);
			default:
			}
		}while(choice != 5);
		input.close();
	}

}
