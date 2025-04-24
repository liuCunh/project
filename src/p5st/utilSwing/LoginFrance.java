package p5st.utilSwing;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginFrance extends JFrame {
    public LoginFrance(){
        setTitle("简单登录页面");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300,200);
        Container contentPane = getContentPane();
        contentPane.setLayout(null);
        JLabel userLabel = new JLabel("用户名");
        userLabel.setBounds(20, 20, 80, 25);
        contentPane.add(userLabel);
        JTextField userText = new JTextField();
        userText.setBounds(100, 20, 150, 25);
        contentPane.add(userText);
        JLabel passLabel = new JLabel("密码");
        passLabel.setBounds(20, 50, 80, 25);
        contentPane.add(passLabel);
        JPasswordField passField = new JPasswordField();
        passField.setBounds(100, 50, 150, 25);
        contentPane.add(passField);
        JButton loginButton = new JButton("登录");
        loginButton.setBounds(50, 80, 80, 25);
        contentPane.add(loginButton);
        JButton cancelButton = new JButton("取消");
        cancelButton.setBounds(140, 80, 80, 25);
        contentPane.add(cancelButton);
        setVisible(true);

        // 按钮添加监听事件
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // 获取用户输入的用户名和密码
                String username = userText.getText().trim();  // 使用Trim() 去除可能的前后空格
                String password = new String(passField.getPassword()).trim();  // 将密码字符串数组转化为字符串，并去除可能的前后空格
                // 设定正确的用户名和密码
                final String CORRECT_USERNAME = "admin";
                final String CORRECT_PASSWORD = "123456";
                // 验证用户名和密码
                if(username.equals(CORRECT_USERNAME) && password.equals(CORRECT_PASSWORD)){
                    JOptionPane.showMessageDialog(null, "登录成功！");

                }else{
                    // 用户名或密码错误，显示错误消息
                    JOptionPane.showMessageDialog(null,"用户名或密码错误，请重试！");
                    // 清空用户名和密码字段, 用户重新输入
                    userText.setText("");
                    passField.setText("");

                }
            }
        });
    }

    public static void main(String[] args) {
        new LoginFrance();
    }
}

