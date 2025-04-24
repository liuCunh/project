package P1st;

public class Multiplicative1 {
    public static void main(String[] args) {
        int i = 1;
        long res = 1;
        do{
            res = i*res;
            i++;
        }while (i <= 10);
        System.out.println("100!="+res);
    }
}
