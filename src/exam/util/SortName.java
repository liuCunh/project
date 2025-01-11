package exam.util;

import java.util.Scanner;

public class SortName {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] name = sc.nextLine().split(" ");
        sort(name);
        for(String str : name){
            System.out.println(str);
        }
    }
    public static void sort(String[] name){
        for (int i=0; i< name.length;i++){
            for(int j = 0; j< name.length - i -1; j++){
                if (name[j].compareTo(name[j+1]) > 0){
                    String tmp = name[j+1];
                    name[j+1] = name[j];
                    name[j] = tmp;
                }
            }
        }
    }
}
