package p5st.utilList;

import java.util.ArrayList;
import java.util.List;

public class StreamOperate {
    public static void main(String[] args) {
        // 创建对象
        Score stu1 = new Score("10001", "刘思雨", "大学英语", 95);
        Score stu2 = new Score("10002", "王利群", "大学英语", 59);
        Score stu3 = new Score("10003", "周凌", "离散数学", 99);
        Score stu4 = new Score("10004", "周伶云", "高等数学", 76);
        List<Score> sc = new ArrayList<Score>();
        sc.add(stu1);
        sc.add(stu2);
        sc.add(stu3);
        sc.add(stu4);
        // 书写方式叫 链式表达式
        sc.stream()
                .filter(stu -> stu.getGrade() >60)  // 过滤 引用参数类型需要重写Predicate接口
                .sorted((o1, o2) -> -(o1.getGrade()-o2.getGrade()))  // 排序 引用数据类型需要重写Comparable接口
                .forEach(stu -> System.out.println(stu.getMsg()));  // 遍历
    }
}
