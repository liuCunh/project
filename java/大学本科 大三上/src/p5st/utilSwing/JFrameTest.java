package p5st.utilSwing;

import javax.swing.*;
import java.awt.*;

public class JFrameTest {
    public static void main(String[] args) {
        JFrame frame = new JFrame("统计点击按钮次数");

        frame.setSize(400, 600);  // 窗口大小
        frame.setLocationRelativeTo(null);  // 窗口居中
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
//        frame.getContentPane().setBackground(Color.WHITE);  // 设置背景

        // 添加按钮
        JButton counterButton = new JButton("计数");
        JLabel counterLabel = new JLabel("0");
        counterButton.addActionListener(e -> {
            String counterStr = counterLabel.getText();
            Integer counter = Integer.valueOf(counterStr);
            counter++;
            counterLabel.setText(String.valueOf(counter));
        });
        FlowLayout flowLayout = new FlowLayout(FlowLayout.CENTER, 10,  10);
        frame.setLayout(flowLayout);
        frame.add(counterButton);
        frame.add(counterLabel);
        frame.setVisible(true);  //显示
    }
}
