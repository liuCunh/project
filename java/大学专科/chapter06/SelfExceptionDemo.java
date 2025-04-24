package chapter06;

class SelfDefineException extends Exception{  // 自定义异常类
	public SelfDefineException() {
		super();
	}
	public SelfDefineException(String str) {
		super(str);
	}
}

class Cal{
	static void sqrt(double d) throws SelfDefineException{
		if(d < 0) {
			throw new SelfDefineException("负数不能开方！");
		}else {
			System.out.println(d+"的平方根为："+Math.sqrt(d));
		}
	}
}

public class SelfExceptionDemo {
	public static void main(String[] args) {
		String a = "123456";
		System.out.println(a.charAt(3));  // 字符串按照索引访问字符
		try {
			Cal.sqrt(4);
			Cal.sqrt(-4);
		}catch(SelfDefineException se) {
			System.out.println("异常");
			se.printStackTrace();
		}finally {
			System.out.println("捕获和处理异常结束！");
		}
	}
}
