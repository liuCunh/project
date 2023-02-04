package chapter04;

public class Practice {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String density = " abca ABC1231 ";
		String density01 = "abc1234";
		String density02 = "ABC1234";
		int a = 520;
		
//		System.out.println(density.length());
//		System.out.println(density.equals(density));  // 字符串内容是否相等
//		System.out.println(density01.equalsIgnoreCase("abc1234"));  // 忽略字母大小写，比是否相等
//		System.out.println(density01.compareTo(density02));
//		System.out.println(density.concat(density01));  // 字符串拼接
//		System.out.println(density.substring(3));  // 字符串的截取
//		System.out.println(density.indexOf("1"));  // 字符串的查找，从前面往后查找
//
//		System.out.println(density.lastIndexOf("1"));  // 从后面往前查找
//		System.out.println(density.toUpperCase());  // 转大写
//		System.out.println(density.toLowerCase());  // 转小写
//		System.out.println(density.charAt(1));  // 字符串的下标操作
//		System.out.println(density.startsWith("abc"));  // python中的startswith()函数, 是否是该字符串为开头
//		System.out.println(density.endsWith("234"));  // Python中的endswith()函数， 是否为该串结尾
//		System.out.println(density.replace("a", "哈哈"));  // 替换字符串，replace(旧， 新)
//		System.out.println(density.replace(density, density01));  // 整体替换
//		System.out.println(density.replaceFirst("a", "haha"));  // 替换第一个
//		System.out.println(density.trim());  // 去掉首尾空格
		System.out.println(String.valueOf(a));  // 数据转换成字符串
	}

}
