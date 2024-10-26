import java.util.Scanner;

class Person {
    String id;
    int level;

    public Person() {
        this.id = "codetree";
        this.level = 10;
    }

    public Person(String id, int level) {
        this.id = id;
        this.level = level;
    }
}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        Person person1 = new Person();
        Person person2 = new Person(sc.next(), sc.nextInt());

        System.out.println("user " + person1.id + " lv " + person1.level);
            System.out.println("user " + person2.id + " lv " + person2.level);
    }
}