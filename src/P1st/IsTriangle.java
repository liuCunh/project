package P1st;

import java.util.Arrays;
import java.util.Scanner;

public class IsTriangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] edges = new int[3];
        for(int i = 0; i<3; i++){
            System.out.print("Place enter triangle edge: ");
            edges[i] = scanner.nextInt();
        }
        Arrays.sort(edges);
        if (edges[0] + edges[1] <edges[2]){
            System.out.println("你输入的三边不能构成三角形！");
        }else{
            System.out.println("你输入的三边能构成三角形！");
        }

    }
}
