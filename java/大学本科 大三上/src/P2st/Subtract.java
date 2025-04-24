package P2st;

public class Subtract {
    // int subtract
    public static int subtract(int a, int b){
        return a - b;
    }
    // double subtract
    public static double subtract(double a, double b){
        return a - b;
    }
    public static void main(String[] args) {
        // int 调用
        System.out.printf("3 - 2=%d\n", subtract(3, 2));
        // double 调用
        System.out.printf("3.14 - 2.98=%.2f", subtract(3.14, 2.98));
    }
}
