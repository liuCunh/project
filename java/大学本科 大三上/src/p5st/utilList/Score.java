package p5st.utilList;

public class Score{
    private String no;  // 学号
    private String name;  // 姓名
    private String course;  // 科目
    private int grade;  //成绩

    public Score(String no, String name, String course, int grade) {
        this.no = no;
        this.name = name;
        this.course = course;
        this.grade = grade;
    }

    public String getNo() {
        return no;
    }

    public void setNo(String no) {
        this.no = no;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }

    public int getGrade() {
        return grade;
    }

    public void setGrade(int grade) {
        this.grade = grade;
    }

    public String getMsg(){
        return "学号：%s 姓名：%s 课程：%s 成绩：%d".formatted(no, name, course, grade);
    }
}
