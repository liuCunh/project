package exam.util;

import java.sql.*;

public class JDBCExam {
    public static void main(String[] args) throws Exception{
        // 加载驱动
        Class.forName("com.mysql.jdbc.Driver");
        Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/testdb?useUnicode=true&characterEncoding=utf8", "root", "");
        // 创建Statement对象
        Statement statement = connection.createStatement();

        // 添加操作
        String book_name = "软件测试";
        String book_author = "李万伦";
        String insertSql = "insert into book(book_name, book_author) values(?, ?)";

        // 预编译执行语句
        PreparedStatement ps = connection.prepareStatement(insertSql);
        ps.setString(1, book_name);
        ps.setString(2, book_author);
        int insertAffect = ps.executeUpdate();
        System.out.println(insertAffect);

        // 查询操作
        String selectSql = "select * from book";
        // 执行Sql语句，返回结果集
        ResultSet rs = statement.executeQuery(selectSql);
        // 得到结果集中的总行数，方便后续时候for循环遍历结果集
        int conlumnCount = rs.getMetaData().getColumnCount();
        // 指针指向第一行的前一行
        while (rs.next()){
            System.out.println(rs.getInt(1));
            System.out.println(rs.getObject(2));
            System.out.println(rs.getString(3));
        }

        // 关闭连接
        rs.close();
        ps.close();
        statement.close();
        connection.close();
    }
}
