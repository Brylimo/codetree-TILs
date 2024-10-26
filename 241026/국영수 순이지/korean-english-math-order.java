import java.util.Scanner;
import java.util.Arrays;

class Student implements Comparable<Student> {
    String name;
    int kor;
    int eng;
    int math;

    public Student(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }

    @Override
    public int compareTo(Student student) {
        if (this.kor == student.kor && this.eng == student.eng) {
            return student.math - this.math;
        }

        if (this.kor == student.kor) {
            return student.eng - this.eng;
        }

        return student.kor - this.kor;
    }
}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
    
        int n = sc.nextInt();
        Student[] students = new Student[n];
        for (int i = 0; i < n; i++) {
            students[i] = new Student(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
        }
    
        Arrays.sort(students);

        for (int i = 0; i < n; i++) {
            System.out.println(students[i].name + " " + students[i].kor + " " + students[i].eng + " " + students[i].math);
        }
    }
}