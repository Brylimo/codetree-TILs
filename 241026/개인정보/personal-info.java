import java.util.Scanner;
import java.util.Arrays;

class Person implements Comparable<Person> {
    String name;
    int height;
    double weight;

    public Person(String name, int height, double weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    @Override
    public int compareTo(Person person) {
        return this.name.compareTo(person.name);
    }
}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
    
        Person[] persons = new Person[5];
        for (int i = 0; i < 5; i++) {
            persons[i] = new Person(sc.next(), sc.nextInt(), sc.nextDouble());
        }

        Arrays.sort(persons);
        System.out.println("name");
        for (int i = 0; i < 5; i++) {
            System.out.println(persons[i].name + " " + persons[i].height + " " + persons[i].weight);
        }
        System.out.println();

        Arrays.sort(persons, (a, b)->b.height - a.height);
        System.out.println("height");
        for (int i = 0; i < 5; i++) {
            System.out.println(persons[i].name + " " + persons[i].height + " " + persons[i].weight);
        }
    }
}