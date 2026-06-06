import java.util.HashMap;
import java.util.Map;

public class Question10_Flyweight {
    static class Flyweight {
        private String intrinsic;

        Flyweight(String s) {
            intrinsic = s;
        }

        public String get() {
            return intrinsic;
        }
    }

    static class Factory {
        Map<String, Flyweight> map = new HashMap<>();

        Flyweight get(String k) {
            return map.computeIfAbsent(k, Flyweight::new);
        }
    }

    public static void main(String[] args) {
        Factory f = new Factory();
        Flyweight a = f.get("X");
        Flyweight b = f.get("X");
        System.out.println(a == b);
    }
}
