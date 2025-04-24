package exam.util;

import java.util.ArrayList;

public class ArrayListTest {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<Integer>();
        nums.add(100);
        nums.add(200);
        nums.add(300);
        // 删除元素对象300
        nums.remove(Integer.valueOf(300));
        // 遍历元素
        for(Integer num: nums){
            System.out.println(num);
        }

    }
}
