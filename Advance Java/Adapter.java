public class Question5_Adapter {
    interface Target {
        String request();
    }

    static class Adaptee {
        String specific() {
            return "Adaptee result";
        }
    }

    static class Adapter implements Target {
        Adaptee a = new Adaptee();

        public String request() {
            return a.specific();
        }
    }

    public static void main(String[] args) {
        Target t = new Adapter();
        System.out.println(t.request());
    }
}
