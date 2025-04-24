//mysql查询
import java.sql.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 加载驱动
        Class.forName("com.mysql.jdbc.Driver");
        Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/testdb", "root", "");
        // 创建Statement对象
        Statement statement = connection.createStatement();
        // 查询操作
        String selectSql = "select * from book";
        // 执行Sql语句，返回结果集
        ResultSet rs = statement.executeQuery(selectSql);
        // 指针指向第一行的前一行
        while (rs.next()){
            System.out.print("id: "+rs.getInt("id"));
            System.out.print(", book_name: "+rs.getObject("book_name"));
            System.out.println(", book_author: "+rs.getString("book_author"));
        }
        // 关闭连接
        rs.close();
        statement.close();
        connection.close();
    }
}
