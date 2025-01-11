package p5st.utilJDBC;

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.util.Properties;

public class DruidMysql {
    public static void main(String[] args)  throws Exception{

        // druid连接数据库原子操作
        Properties pro = new Properties();
        // 采用类加载器ClassLoader得到指定文件名properties文件的输入流
        pro.load(DruidMysql.class.getClassLoader().getResourceAsStream("druid.properties"));
        // 用DruidDataSourceFactory的createDataSource方法获取连接池对象
        DataSource ds = DruidDataSourceFactory.createDataSource(pro);
        Connection connection = ds.getConnection();

        connection.setAutoCommit(false);  // 取消事务的自动提交
        try{
            String sql = "update customer set age=33 where id =1";
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.executeUpdate();
//            System.out.println(1/0);  // 模拟程序错误
            connection.commit();  // 提交事务
        }catch (Exception e){
            e.printStackTrace();
            connection.rollback();  // 回滚数据库
        }finally {
            connection.setAutoCommit(true);
            connection.close();
        }

    }
}
