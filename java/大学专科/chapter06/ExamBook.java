package chapter06;

class Book {
	private String bo_class, bo_name;
	public static int nums = 10;
	
	public Book(String bo_class, String bo_name) {
		this.bo_class = bo_class;
		this.bo_name = bo_name;
	}
	
	public static void display() {
		System.out.println("书籍剩余量："+nums);
	}
}

public class ExamBook {
	public static void main(String[] args) {
		Book book = new Book("计算机", "Java程序设计基础");
		book.display();
	}
}
