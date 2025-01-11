package p3st.util.dataDefined;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Date1 {
    public static void main(String[] args) {
        double principal = 1000;
        double dailyRate = 0.00001;
        LocalDate depositDate = LocalDate.of(2011, 10, 12);
        System.out.printf("存款日期: %s, 存款利息: %s, 存款本金：%.2f\n", depositDate, calculateInterest(principal, dailyRate, depositDate), principal);
    }
    /**
     * 计算利息
     * principal 本金
     * dailyRate 每日利率
     * depositDate 存款日期
     * return 存款利息
     */
    public static double calculateInterest(double principal, double dailyRate, LocalDate depositDate) {
        LocalDate currentDate = LocalDate.now();  // 最大天数
        long days = depositDate.until(currentDate, ChronoUnit.DAYS);  // 计算天数
        return principal * dailyRate * days;
    }
}
