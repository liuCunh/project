package p5st.utilFile;

import java.io.File;
import java.io.IOException;

public class CreateTxt {
    public static void main(String[] args) throws IOException {
        File f1 = new File("test");
        if(!f1.exists()) {
            if (f1.mkdir()) {
                System.out.println(f1.getAbsolutePath() + "创建成功！");
                File f2 = new File(f1, "my.txt");
                try {
                    f2.createNewFile();
                } catch (IOException e) {
                    System.out.println(e.toString());
                }
                System.out.println(f2.getAbsolutePath() + "创建成功");
            }
        }else {
            System.out.println("目录" + f1.toString() + "已经存在！");
        }
    }
}
