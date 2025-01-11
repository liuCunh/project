package P1st;

public class RoadTest {
    public static void main(String[] args) {
        RoadTest demo = new RoadTest();
        demo.sort(0,0);
        demo.sort(10,9);
        demo.sort(10,6);
    }
    void sort(int i, int j){
        int m, n, k;
        m = n = k =0;
        while (i++ < 11){
            if(j<5){
                m++;
                break;
            }else{
                if(j<8){
                    n++;
                }else{
                    k++;
                }
            }
            i++;
        }
        System.out.printf("m=%d, n=%d, k=%d\n", m, n, k);
    }
}
