package p5st.utilNetwork;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class ClientDemo {
    public static void main(String[] args) throws IOException {
        Socket s = new Socket("127.0.0.1", 10005);
        // 封装文本文件数据
        BufferedReader br = new BufferedReader(new FileReader("inFileDemo\\clientDemo.txt"));
        // 封装输出流写数据
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));

        String line;
        while((line= br.readLine()) != null){
            bw.write(line);
            bw.newLine();
            bw.flush();
        }

        s.shutdownOutput();

        // 接收反馈
        BufferedReader brClient = new BufferedReader(new InputStreamReader(s.getInputStream()));
        String data = brClient.readLine();
        System.out.println("服务器的反馈："+data);

        br.close();
        s.close();
    }
}
class ServerDemo{
    public static void main(String[] args) throws IOException {
        // 创建服务器Socket对象
        ServerSocket ss = new ServerSocket(10005);

        while(true){
            // 监听客户端连接，返回一个对应的Socket对象
            Socket s = ss.accept();
            // 为每一个客户端开启一个线程
            new Thread(new ServerThread(s)).start();

        }
    }
}
class ServerThread implements Runnable{
    private Socket s;

    public ServerThread(Socket s) {
        this.s = s;
    }

    @Override
    public void run() {
        // 接收数据写到文本文件
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
//            BufferedWriter bw = new BufferedWriter(new FileWriter("serverDemo.txt"));

            // 解决名称冲突问题
            int count = 0;
            File file = new File("serverDemo["+count+"].txt");
            while(file.exists()){
                count++;
                file = new File("serverDemo["+count+"].txt");
            }
            BufferedWriter bw = new BufferedWriter(new FileWriter(file));

            String line;
            while((line = br.readLine())!=null){
                bw.write(line);
                bw.newLine();
                bw.flush();
            }
            // 给出反馈
            BufferedWriter bwServer = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
            bwServer.write("文件上传成功");
            bwServer.newLine();
            bwServer.flush();

            // 释放资源
            s.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}