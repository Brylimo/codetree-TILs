import java.util.Scanner;
import java.util.Arrays;

class Person {
    String name;
    int height;
    int weight;

    public Person(String name, int height, int weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }
}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
    
        Person[] persons = new Person[n];
        for (int i = 0; i < n; i++) {
            persons[i] = new Person(sc.next(), sc.nextInt(), sc.nextInt());
        }

        Arrays.sort(persons, (a, b) -> a.height - b.height);

        for (int i = 0; i < n; i++) {
            System.out.println(persons[i].name + " " + persons[i].height + " " + persons[i].weight);
        }
    }
}