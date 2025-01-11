package P2st;

public class Calculate {
    // 加法定义
    public static int add(int a, int b){
        return a + b;
    }
    // 乘法定义
    public static int multiply(int a, int b){
        return a * b;
    }
    // 方法调用
    public static void main(String[] args) {
        System.out.println(add(1, 2));
        System.out.println(multiply(3, 4));
    }
}
