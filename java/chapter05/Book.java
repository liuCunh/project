package chapter05;

public class Book {	
	public static void main(String[] args) {
		Books book = new Books("金瓶梅", "001", "秦修容", "中华书局", "19980301", 10, 268.00);
		book.detail();
	}
}
class Books{
	String boName, boID, boAuthor, boPublish, boTime;
	int boPage;
	double boPrice;
	public Books(String name, String ID, String author, String publish, String time, int page, double price) {
		this.boName = name;
		this.boID = ID;
		this.boAuthor = author;
		this.boPublish = publish;
		this.boTime = time;
		this.boPage = page;
		this.boPrice = price;
		if(page < 250) {
			System.out.println("");
		}
	}
	
	public void detail() {
		System.out.println(boName+","+boID+","+boAuthor+","+boPublish+","+boTime+","+boPage+","+boPrice);
	}
}
