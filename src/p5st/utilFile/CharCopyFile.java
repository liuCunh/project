package p5st.utilFile;

import java.io.*;

public class CharCopyFile {
    public static void main(String[] args) throws IOException {
        File f1 = new File("inFileDemo\\customer10.txt");
        File f2 = new File("inFileDemo\\customer2.txt");
        copyFile(f1, f2);
    }
    public static void copyFile(File inFile,File outFile) throws IOException{
        // 创建字符缓冲流
        BufferedReader bufferedReader = new BufferedReader(new FileReader(inFile));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(outFile));
        String line;
        StringBuilder stringBuffer = new StringBuilder();
        while((line = bufferedReader.readLine()) != null){
            stringBuffer.append(line).append("\n");
        }
        // 写入文件
        bufferedWriter.write(stringBuffer.toString());

        bufferedReader.close();
        bufferedWriter.close();
    }
}
