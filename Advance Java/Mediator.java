import java.util.ArrayList;
import java.util.List;

public class Question14_Mediator {
    interface Mediator {
        void send(String msg, Colleague c);
    }

    static class ChatRoom implements Mediator {
        List<Colleague> users = new ArrayList<>();

        public void register(Colleague c) {
            users.add(c);
        }

        public void send(String msg, Colleague s) {
            for (Colleague c : users)
                if (c != s)
                    c.receive(msg);
        }
    }

    static abstract class Colleague {
        Mediator med;

        Colleague(Mediator m) {
            med = m;
        }

        abstract void receive(String m);

        void send(String m) {
            med.send(m, this);
        }
    }

    static class User extends Colleague {
        String name;

        User(String n, Mediator m) {
            super(m);
            name = n;
        }

        void receive(String m) {
            System.out.println(name + " received: " + m);
        }
    }

    public static void main(String[] args) {
        ChatRoom room = new ChatRoom();
        User a = new User("A", room);
        User b = new User("B", room);
        room.register(a);
        room.register(b);
        a.send("Hello");
    }
}
