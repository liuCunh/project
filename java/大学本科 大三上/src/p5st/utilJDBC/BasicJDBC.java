package p5st.utilJDBC;

import java.sql.*;

public class BasicJDBC {
    public static void main(String[] args) throws Exception {
        // 加载驱动
        Class.forName("com.mysql.jdbc.Driver");
        // 连接数据库
        Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/xsgl", "root",  "");
        // 打印数据库名字
        System.out.println(connection.getCatalog());
        // Statement对象发送SQL语句
        Statement statement = connection.createStatement();
        // sql
        String sql = "select * from fruits;";
        // 执行sql
        ResultSet resultSet = statement.executeQuery(sql);
        // 遍历元素
        // 打印表头 metaData 表头集合
        ResultSetMetaData metaData = resultSet.getMetaData();
        for(int i=1; i<=metaData.getColumnCount(); i++){
            System.out.print(metaData.getColumnName(i)+"\t");
        }
        System.out.println();
        // 打印记录 getObject()字段索引，从1开始，
        while(resultSet.next()){
            System.out.print(resultSet.getObject(1)+"\t");  // 索引访问记录
            System.out.print(resultSet.getObject("fruit_name")+"\t");  // 字段名访问记录
            System.out.print(resultSet.getDouble(3)+"\t");  // 直接认定为浮点数
            System.out.print(resultSet.getInt(4)+"\t\n");
        }

    }
}
