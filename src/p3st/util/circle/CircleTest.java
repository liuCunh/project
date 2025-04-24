package p3st.util.circle;

public class CircleTest {
    public static void main(String[] args) {
        double radius = 2;
        Circle circle = new Circle(radius);
        System.out.printf("半径为：%.2f 的圆面积为 %.2f", radius, circle.calArea());
    }
}
