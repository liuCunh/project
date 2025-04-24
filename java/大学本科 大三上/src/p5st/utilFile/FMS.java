package p5st.utilFile;

import java.io.File;
import java.io.IOException;

/*
 * 文件的 增删改查
 * mkdir 创建单独目录，mkdirs创建多级目录，delete删除文件
 * */
public class FMS {
    public static void main(String[] args) throws IOException {
        // 创建文件
        File f1 = new File("src\\p5st\\utilFile\\file\\cc");  // 文件对象
//        System.out.println("f1");
//        File f1c = new File("src\\p5st\\utilFile\\file\\tmp.txt");
//        f1c.createNewFile();  // 创建文件
//        File f2c = new File("src\\p5st\\utilFile\\file\\aa") ;
//        f2c.mkdir();  // 创建目录
//        File f3c = new File("src\\p5st\\utilFile\\file\\cc\\dd");
//        f3c.mkdirs();
        // 遍历文件
//        if (f1.isDirectory()){  // 判断文件是否存在
//            String[] names = f1.list();  // 获取目录下的所有文件名
//            for (String name : names) {
//                System.out.println(name);
//            }
//        }
//        fileDir(f1);
//        deleteDir(f1);

        deleteDir(f1);
    }

    // 输出文件绝对路径
    public static void fileDir(File dir) {
        File[] files = dir.listFiles();  // 对象数字文件
        for (File file : files) {
            if (file.isDirectory()) {
                fileDir(file);  // 如果是目录，递归调用文件名
            }
            System.out.println(file.getAbsolutePath());  // 文件决定路径
        }
    }

    // 删除文件
    public static void deleteDirNot(File dir) {
        if (dir.exists()) {  // 对象是否存在
            File[] files = dir.listFiles();  // 对象数字文件
            for (File file : files) {
                if (file.isDirectory()) {
                    deleteDirNot(file);  // 如果是目录，递归调用文件名
                } else {
                    file.delete();
                }
            }
            dir.delete();
        }
    }

    public static void createFile(File fileDir) throws IOException {
        if (!fileDir.exists()) {
            File f1c = new File("src\\p5st\\utilFile\\file\\tmp.txt");
            f1c.createNewFile();  // 创建文件
            File f2c = new File("src\\p5st\\utilFile\\file\\aa");
            f2c.mkdir();  // 创建目录
        }
    }
    // 打印文件
    public static void showDir(File fileDir){
        File[] files = fileDir.listFiles();  // 目录对象
        if(files == null || files.length == 0){
            System.out.println("读取文件为空！");
             return; // 传入一个空文件夹或者文件时就直接删除
        }
        System.out.println("|- " + fileDir.getName());  // 打印文件名
        for (File file : files){
            if (file.isFile()){
                // 如果是文件输出文件名字
                System.out.println("|- " + file.getName());
            }else{
                // 如果是文件夹 递归调用
                showDir(file);
            }
        }
    }

    public static void deleteDir(File fileDir){
        File[] files = fileDir.listFiles();
        if(files == null || files.length == 0){
            fileDir.delete();  // 传入一个空文件夹或者文件时就直接删除
        }
        // 如果是目录就直接 递归删除
        for(File file: files){
            if (file.isDirectory()){
                deleteDir(file);  // 删除目录
            }else{
                file.delete();  // 删除文件
            }
        }
        fileDir.delete();   // 删除最外层目录
        System.out.println("删除成功！");
    }

}
