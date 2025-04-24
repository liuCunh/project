package chapter05.ATM;
import java.util.Date;
public class AccountCard {
// 年利率；账号、持卡人姓名、身份证号码、地址；交易金额、交易日期、余额
	private static double interest;
	private String account, name, id, address;
	private double balance;
	private double DWAmount;
	private Date DWDate;
	
	// 无参数的构造方法
	public AccountCard() {  // 初始化持卡人信息
		super();
		this.account = "1111111110";
		this.name = "王朝";
		this.id = "321020199809181215";
		this.address = "重庆市江北区红石路255号";
		this.balance = 0;
	}
	
	// 重载构造，带参数的构造方法
	public AccountCard(String account, String name, String id, String address, double balance) {
		super();
		this.account = account;
		this.name = name;
		this.id = id;
		this.address = address;
		this.balance = balance;
	}
	
	public void menu() {  // 菜单选项
		System.out.println("\n欢迎使用银行ATM系统2.0版本");
		System.out.println("\t1. 存 款");
		System.out.println("\t2. 取 款");
		System.out.println("\t3. 购物付款");
		System.out.println("\t4. 查 询");
		System.out.println("\t5. 退 出");
		System.out.println("选择请输入数字[1-5]：");
	}
	
	// 静态getter()
	public static double getInterest() {
		return interest;
	}
	
	// 静态setter()
	public static void setInterest(double interest) {
		AccountCard.interest = interest;
	}
	
	public String getAccount() {
		return account;
	}
	
	public void setAccount(String account) {
		this.account = account;  // 当前类实例
	}
	
	public String getName() {
		return name;
	}
	
	public String getId() {
		return id;
	}
	
	public void setId(String id) {
		this.id = id;
	}
	
	public String getAddress() {
		return address;
	}
	
	public void setAddress(String address) {
		this.address = address;
	}
	
	public void setbalance(Double balance) {
		this.balance = balance;
	}
	
	// 存款、取款、查询；购物支付、禁止透支；取款行为
	public void deposit(double cash) {
		System.out.println("= = = = = = =存款= = = = = = = = =");
		System.out.println("您的卡号："+this.account);
		System.out.println("您的姓名："+this.name);
		System.out.println("您的余额："+this.balance);
		System.out.println("现存入："+cash);
		this.DWAmount = cash;
		balance = this.balance+cash;  // 余额自动计算
		System.out.println("最终余额:"+this.balance);
		this.DWDate = new Date();  // 存入当天的日期
		System.out.println("存款日期："+this.DWDate);
	}
	
	// 存款行为
	public void withdraw(double cash) {
		System.out.println("= = = = = = =取款= = = = = = = = =");
		System.out.println("您的卡号："+this.account);
		System.out.println("您的姓名："+this.name);
		System.out.println("您的余额："+this.balance);
		System.out.println("现取出入："+cash);
		this.DWAmount = cash;
		if((this.balance - cash) > 0) {  // 禁止透支
			this.balance = this.balance - cash;  // 余额自动计算
			System.out.println("最终余额："+this.balance);
		}else {
			System.out.println("取出数额太大！请从新输入。");
		}
		this.DWDate = new Date();  // 记录当天时间
		System.out.println("取款日期："+this.DWDate);
	}
	
	// 类的查询行为
	public void query() {
		System.out.println("= = = = = = =查询= = = = = = = = =");
		System.out.println("您的卡号："+this.account);
		System.out.println("您的姓名："+this.name);
		System.out.println("最终余额是："+this.balance);
		this.DWDate = new Date();  // 记录当天时间
		System.out.println("查询日期："+this.DWDate);
	}
	
	// 付款行为
	public void purchase(double payment) {
		System.out.println("= = = = = = =购物= = = = = = = = =");
		System.out.println("您的卡号："+this.account);
		System.out.println("您的姓名："+this.name);
		System.out.println("最终余额是："+this.balance);
		System.out.println("现付出："+payment);
		this.DWAmount = payment;
		if ((this.balance - payment) > 0) {
			this.balance = this.balance - payment;
			System.out.println("最终余额："+this.balance);
		}else {
			System.out.println("余额不足！");
		}
		this.DWDate = new Date();  // 记录当前日期
		System.out.println("付款日期："+this.DWDate);
		
	}
}
