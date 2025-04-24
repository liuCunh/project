package p5st.utilList;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class SetOperate {

    public static void main(String[] args) {
        Score stu0 = new Score("10001", "刘思雨", "大学英语", 95);
        Score stu1 = new Score("10002", "王利群", "大学英语", 59);
        Score stu2 = new Score("10003", "周凌", "离散数学", 99);
        Score stu3 = new Score("10004", "周伶云", "高等数学", 76);
        Set<Score> score = new HashSet<Score>();
        // 添加元素
        score.add(stu0);
        score.add(stu1);
        score.add(stu2);
        score.add(stu3);

        // 迭代器对象单个访问
        Iterator<Score> iterator = score.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next().getMsg());
        }

        score.forEach(stu -> System.out.println(stu.getMsg()));  // 直接引用Score中的getMsg方法
        score.remove(stu2);
        System.out.println("------------------------删除后结果------------------------");
        score.forEach(stu -> System.out.println(stu.getMsg()));
    }
}

