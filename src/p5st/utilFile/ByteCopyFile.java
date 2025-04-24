package p5st.utilFile;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class ByteCopyFile {
    public static void main(String[] args) throws IOException {
        File inF = new File("inFileDemo");
        File outF = new File("outFileDemo");

        fCoy(inF, outF);
    }

    public static void fCoy(File inF, File outF) throws IOException {

        // 输出文件不存在
        if (!outF.exists()){
            outF.mkdir();
        }
        File[] files = inF.listFiles();

        // 输入文件为空
        if(files==null){
            return;
        }
        for(File file: files){
            File newF = new File(outF, file.getName());
            if (file.isDirectory()){
                // 文件夹
                fCoy(file, newF);
            }else {
                // 文件
                FileInputStream fis = new FileInputStream(file);
                FileOutputStream fos= new FileOutputStream(newF);
                // 循环写入
                int i = 0;
                while((i=fis.read())!=-1){
                    fos.write(i);
                }

                fis.close();
                fos.close();

            }
        }

    }
}


