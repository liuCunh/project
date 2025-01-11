package p3st.util;

public class CountChar {
    public static void main(String[] args) {
        String str = "abcd abcd abcd";
        int count = 0;  // 统计数量
        int ind;  // 记录下标
        do{
            ind = str.indexOf("c");
            str = str.substring(ind+1);
            count++;
        }while(ind != -1);
        // 查找文本下标
        System.out.printf("c 出现次数：%d\n", count);
    }
}
