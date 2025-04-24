package P1st;

public class CharAndASCII {
    public static void main(String[] args) {
        // 转义字符
        char ch3 = '\n'; //换行
        char ch4 = '\\'; // 反斜杠 \ 本身

        // unicode 转义字符
        System.out.println('\101');  // \ddd d为八进制数 ASCII字符转换
        System.out.println('\u4E2D'); // \udddd d为十六进制数 unicode字符转换
        System.out.println('\u56FD');

        final int KEY = -1;  // 生命常量

        char a = 'A';
        // \u000a a = 'Y';
        System.out.println(a);

        System.out.println(0.1+0.2);
    }
}
