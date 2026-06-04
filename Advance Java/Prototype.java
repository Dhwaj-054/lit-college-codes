public class Question3_Prototype {
    static class Prototype implements Cloneable {
        String data;

        Prototype(String d) {
            data = d;
        }

        public Prototype clone() {
            try {
                return (Prototype) super.clone();
            } catch (Exception e) {
                return null;
            }
        }

        public String toString() {
            return data;
        }
    }

    public static void main(String[] args) {
        Prototype p1 = new Prototype("Original");
        Prototype p2 = p1.clone();
        System.out.println(p2);
    }
}
