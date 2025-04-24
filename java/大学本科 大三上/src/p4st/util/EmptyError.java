package p4st.util;

public class EmptyError {
    public static void main(String[] argk) {
        String score = "100 92 60 72";
        calculateAverage(score);
    }
    public static void calculateAverage(String str){
        if(str.trim().isEmpty()){
            System.out.println("字符串不能为空！");
        }else{
            try{
                String[] score = str.split(" ");
                int sum=0, count=0;
                for(String num: score){
                    int tmp = Integer.parseInt(num);
                    sum += tmp;
                    count++;
                }
                System.out.printf("average: %.2f", (double) sum/count);
            }catch(NumberFormatException e){
                System.out.println("存在无法解析的字符串，请检查参数");
            }

        }
    }
}
