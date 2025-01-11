package p5st.utilJDBC;

import java.sql.*;

public class UpdateMysql {
    public static void main(String[] args) throws Exception{
        Class.forName("com.mysql.jdbc.Driver");
        String url = "jdbc:mysql://localhost:3306/testdb";
        String login = "root";
        String password = "";
        Connection connection = DriverManager.getConnection(url, login, password);
        // 所有sql语句都建立在Statement对象之上
        Statement statement = connection.createStatement();
        String updateSql = "update customer set age=21 where name='jack'";
        int updateResult = statement.executeUpdate(updateSql);  // 返回被影响的行数, 其中增，删，改操作都能使用

        String insertSql = "insert into customer(name,age) values('smith', 30)";
        int insertResult = statement.executeUpdate(insertSql);

        String deleteSql = "delete from customer where id=3";
        System.out.printf("Update收到影响的行数: %d, Insert收到影响的行数: %d",updateResult, insertResult);
        // 关闭创建对象
        statement.close();
        connection.close();
    }
}
