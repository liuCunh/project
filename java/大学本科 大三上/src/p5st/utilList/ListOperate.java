package p5st.utilList;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ListOperate {
    /**
     * Collection单列集合 Map双列集合
     */
    public static void main(String[] args) {
        List<Score> scoreList = new ArrayList<Score>();
        // 创建对象
        Score stu1 = new Score("10001", "刘思雨", "大学英语", 95);
        Score stu2 = new Score("10002", "王利群", "大学英语", 59);
        Score stu3 = new Score("10003", "周凌", "离散数学", 99);
        Score stu4 = new Score("10004", "周伶云", "高等数学", 76);
        // 添加元素
        scoreList.add(stu1);
        scoreList.add(stu2);
        scoreList.add(stu3);
        scoreList.add(stu4);
        // 元素是否存在 返回boolean值
        System.out.println(scoreList.contains(stu1));
        // 获取元素索引 返回数字下标
        System.out.println(scoreList.indexOf(stu2));
        // 获取长度
        System.out.println("ArrayList长度="+scoreList.size());
        // 遍历元素
        for(Score sc : scoreList){
            System.out.printf("姓名: %s, 科目: %s, 成绩: %d\n", sc.getName(), sc.getCourse(), sc.getGrade());
        }
        System.out.println("----------迭代器遍历集合----------");
        // 创建迭代器
        Iterator<Score> it = scoreList.iterator();
        while(it.hasNext()){
            Score sc = it.next();
            System.out.printf("姓名: %s, 科目: %s, 成绩: %d\n", sc.getName(), sc.getCourse(), sc.getGrade());
        }

        scoreList.remove(2);  // 删除第三个元素
        System.out.println("删除第三个成绩后结果");
        scoreList.forEach(sc -> System.out.printf("姓名: %s, 科目: %s, 成绩: %d\n", sc.getName(), sc.getCourse(), sc.getGrade()));
        Score sc3 = scoreList.get(2);
        System.out.printf("列表中第三个元素为：%s，%s，%d", sc3.getName(), sc3.getCourse(), sc3.getGrade());
    }
}
