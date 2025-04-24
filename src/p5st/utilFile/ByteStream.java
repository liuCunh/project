package p5st.utilFile;

import java.io.*;

public class ByteStream {
    public static void main(String[] args) throws IOException {
//        File f1 = new File("test\\my.txt");
//        // 创建输入流
//        FileInputStream in = new FileInputStream("test\\my.txt");
//        int b = 0;  // 记住每个读取的字节
//        while(true){
//            b = in.read();  // 按照字节读入 读出来为ASCII码
//            if (b == -1){  // 当文件结束时默认为-1
//                break;
//            }
//            System.out.println((char)b);
//        }
//
//        //覆盖写入
//        OutputStream out = new FileOutputStream(f1);
//        String str = "我是一行字符串";
//        byte[] cs = str.getBytes();  // 将字符串转化为 单个字符数组
//        for(int i=0; i < cs.length; i++){
//            out.write(cs[i]);
//        }

        File srcDir = new File("inFileDemo");
        File desDir = new File("outFileDemo");
        copyDir(srcDir, desDir);
    }

    // 文件复制
    public static void copyDir(File srcDir, File desDir) throws IOException {
        // 复制文件夹不存在则创建
        if (!desDir.exists()){
            desDir.mkdir();
        }
        File[] files = srcDir.listFiles();
        if (files==null || files.length==0){
            return;  // 源文件为空直接退出
        }
        // 不为空循环复制文件夹跟文件
        for(File file: files){
            File newDir = new File(desDir, file.getName());
            if (file.isDirectory()){  // 如果为文件夹则递归处理
                copyDir(file, newDir);
            }else {
                // 创建输入流，用于读取文件内容
                FileInputStream fis = new FileInputStream(file);
                // 创建输出流，用于写文件
                FileOutputStream fos = new FileOutputStream(newDir);
                int len=0;
                while((len = fis.read()) != -1){ // 未到最后且循环读入
                    fos.write(len);  // 将输入写入目标文件
                }
                // 关闭流
                fis.close();
                fos.close();
            }
        }
    }
}
