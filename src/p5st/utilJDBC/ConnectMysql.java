package p5st.utilJDBC;

import java.sql.*;

public class ConnectMysql {
    public static void main(String[] args) throws Exception {
        // 注册驱动
        Class.forName("com.mysql.jdbc.Driver");
        String url = "jdbc:mysql://localhost:3306/testdb";
        String login = "root";
        String password = "";
        Connection connection = DriverManager.getConnection(url, login, password);
        System.out.println(connection);
    }
}
