package p5st.utilJDBC;

import java.sql.*;

public class SelectMysql {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.jdbc.Driver");
        Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "");
        Statement statement = connection.createStatement();

        String sql = "select * from customer";
        ResultSet rs = statement.executeQuery(sql);  // 将查询结果放入结果集中

        while(rs.next()){
            System.out.printf("id: %d\t name: %s\t age: %d\n", rs.getInt(1), rs.getString("name")
            , rs.getInt("age"));
        }
        rs.close();
        statement.close();
        connection.close();
    }
}
