package p4st.util;

public class Multiply {
    public static void main(String[] args) {
        int a=3,b=999;
        try{
            multiply(a, b);
        }catch (IllegalArgumentException e){
            System.out.println(e.getMessage()); // 获取抛出信息
        }
    }
    public static void multiply(int a, int b){
        if (!(0< a && a<100) || !(0<b && b<100)){
            throw new IllegalArgumentException("错误信息：参数a（或者）b必须在0~100之间。");
        }
        System.out.printf("%d * %d = %d", a, b, a*b);
    }
}
