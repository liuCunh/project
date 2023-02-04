package chapter05;

public class AbstractMethod {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}

// 定义一个抽象类，该方法不能被实例化
abstract class Abs{
	// 定义一个抽象方法
	public abstract void test();
}
// 继承抽象方法
class AbsChild extends Abs{
	String name;
	public AbsChild() {
		this.name= "张三";
	}
	public void test() {
		
	}
}

