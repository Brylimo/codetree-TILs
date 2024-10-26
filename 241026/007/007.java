import java.util.Scanner;

class BriefCase {
    String code;
    String location;
    int time;

    public BriefCase(String code, String location, int time) {
        this.code = code;
        this.location = location;
        this.time = time;
    }
}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        BriefCase b = new BriefCase(sc.next(), sc.next(), sc.nextInt());

        System.out.println("secret code : " + b.code);
                System.out.println("meeting point : " + b.location);
                        System.out.println("time : " + b.time);
    }
}