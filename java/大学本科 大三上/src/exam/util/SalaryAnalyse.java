package exam.util;

import java.util.Arrays;

public class SalaryAnalyse {
    public static void main(String[] args) {
        double[] salary = {8900.25, 7256.27, 6547.11, 7234.16, 6998.23};
        Arrays.sort(salary);  // 将工资数组排序
        // 格式化工资数组
        System.out.printf("最高工资：%.2f, 最低工资: %.2f, 平均工资: %.2f",
                salary[salary.length-1], salary[0], Arrays.stream(salary).sum() / salary.length);
    }
}
