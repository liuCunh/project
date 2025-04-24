package chapter01;

public class Practice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		boolean a = true;
//		byte b = 15;
//		char c = 'A';
//		float d = 3.14f;
//		String e = "This is a constant string";
//		System.out.println("布尔型= "+a);
//		System.out.println("整形= "+b);
//		System.out.println("字符型= "+c);
//		System.out.println("浮点型= "+d);
//		System.out.println("字符串型= "+e);
//		
//		int i = 5;
//		long j = i;
//		
//		// 强转类型
//		short k = (short)i;
//		
//		int i2 = 50000000;
//		long j2 = i2 * 100L;
//		System.out.println(j2);
		
		String str = "123";
		int ing = Integer.parseInt(str);  // 将字符串数字转化为整形数字
		float F = Float.parseFloat(str);
		double d1 = Double.parseDouble(str);
		long L = Long.parseLong(str);
		System.out.println(ing);
		System.out.println(F);
		System.out.println(d1);
		System.out.println(L);
		
		int ab = 5;
		String temp = String.valueOf(ab);
//		String s = String.valueOf(ab);
//		String g = Integer.toString(ab);
//		String y = ""+ab;
		
		double dou = 3.14;
		String dou1 = String.valueOf(dou);
		String dou2 = Double.toString(dou);
		String dou3 = ""+dou;
		
		float flo = 3.14f;
		String flo1 = String.valueOf(flo);
		String flo2 = Float.toString(flo);
		String flo3 = ""+flo;
		
		
		
		
	}

}
