package p5st.utilNetwork;

import java.io.*;
import java.net.*;

public class Client {
    public Client(){
        try{
            String s;
            Socket socket = new Socket("localhost", 8269);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(),true);
            BufferedReader line = new BufferedReader(new InputStreamReader(System.in));
            while(true){
                System.out.println("请向服务器输出一条字符串");
                s = line.readLine();
                out.println(s);  // 向服务器发出信息
                s = in.readLine().trim();  // 收到服务发来的信息
                System.out.println("服务器返回的信息是："+s);
                if(s.equals("BYE")){
                    out.println("BYE");
                    line.close();
                    in.close();
                    socket.close();
                    break;
                }
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        new Client();
    }
}
