package p5st.utilNetwork;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class AskServer {
    public static void main(String[] args) {
        // 创建DataGramSocket,用于发送跟接受数据
        DatagramSocket socket = null;
        try{
            socket = new DatagramSocket(8888);
            Scanner input = new Scanner(System.in);
            while(true){
                // 准备空数据包，用来接收数据
                byte[] buf = new byte[1024];
                DatagramPacket packet = new DatagramPacket(buf, buf.length);
                // 接收空数据包
                socket.receive(packet);
                // 输出信息
                String info = new String(packet.getData(), 0, packet.getLength());
                System.out.println("客户端请求："+info);
                // 判读是否退出
                if ("bye".equals(info)){
                    break;
                }
                // 发送数据
                String result = input.nextLine();
                byte[] buf2 = result.getBytes();
                DatagramPacket packet2 = new DatagramPacket(buf2, buf2.length, packet.getAddress(), packet.getPort());
                socket.send(packet2);
            }

        } catch (SocketException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            socket.close();
        }
    }
}
