package chapter04;

public class Practice01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StringBuffer a = new StringBuffer("");
		System.out.println(a);
		System.out.println(a.append("HelloWorld!"));
//		System.out.println(a.insert(5, " "));  // 在index后面插入
		System.out.println(a.delete(5, 10));  // 从下标为5的后面到10截止，包括10，前开后闭
		System.out.println(a.reverse());
	}

}
