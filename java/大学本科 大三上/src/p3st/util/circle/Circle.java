package p3st.util.circle;

public class Circle {
    private static double PI; // 圆周率
    private double radius;  // 半径
    static{
        PI = 3.14;
    }
    public Circle(double radius){
        this.radius = radius;
    }
    public double calArea(){
        return radius * radius * PI;
    }
}
