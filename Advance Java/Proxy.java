public class Question11_Proxy {
    interface Subject {
        String request();
    }

    static class RealSubject implements Subject {
        public String request() {
            return "Real";
        }
    }

    static class Proxy implements Subject {
        RealSubject real;

        public String request() {
            if (real == null)
                real = new RealSubject();
            return real.request();
        }
    }

    public static void main(String[] args) {
        Subject s = new Proxy();
        System.out.println(s.request());
    }
}
