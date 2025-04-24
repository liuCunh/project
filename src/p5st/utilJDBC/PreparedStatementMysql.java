package p5st.utilJDBC;

import java.sql.*;

public class PreparedStatementMysql {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.jdbc.Driver");
        Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb?useUnicode=true&characterEncoding=utf8", "root", "");
        String sql = "select * from customer where name=?";  // 用 ？ 表示占位符

        // 避免SQL注入
        PreparedStatement ps = connection.prepareStatement(sql);
        ps.setInt(1, 20);  // 表示 第一个占位符 的参数值为20
//        ps.setString(1, "tom");  // 表示 第一个占位符 的参数值为20

        ResultSet rs = ps.executeQuery();

        while(rs.next()){
            System.out.printf("id: %d\t name: %s\t age: %d\n", rs.getInt(1), rs.getString("name")
                    , rs.getInt("age"));
        }
        rs.close();
        ps.close();
        connection.close();
    }

}
