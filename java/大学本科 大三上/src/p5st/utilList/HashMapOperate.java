package p5st.utilList;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class HashMapOperate {
    public static void main(String[] args) {
        // 创建对象
        Score stu1 = new Score("10001", "刘思雨", "大学英语", 95);
        Score stu2 = new Score("10002", "王利群", "大学英语", 59);
        Score stu3 = new Score("10003", "周凌", "离散数学", 99);
        Score stu4 = new Score("10004", "周伶云", "高等数学", 76);
        Map<String, String> map = new HashMap<String, String>();
        map.put(stu1.getNo(), stu1.getMsg());
        map.put(stu2.getNo(), stu2.getMsg());
        map.put(stu3.getNo(), stu3.getMsg());
        map.put(stu4.getNo(), stu4.getMsg());
        // 遍历Map
        map.forEach((key, value) -> System.out.println(key+" : "+value));
        // 删除Map元素
        map.remove("10001");
        System.out.println("---------- 删除后结果 ---------");
        // 遍历Map 在集合中存储着单个的键值对 eg：（{key:value}, {key:value}, ...}）
        Set<Map.Entry<String, String>> entrySet = map.entrySet();
        for(Map.Entry<String, String> entry: entrySet){
            String key = entry.getKey();  // 获取key
            String value = entry.getValue();  // 获取值
            System.out.println(key+" : "+value);
        }
        // 获取所有的key
        System.out.println(map.keySet());
        // 通过key访问
        System.out.println(map.get("10002"));
    }
}
