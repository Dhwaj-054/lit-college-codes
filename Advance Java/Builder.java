public class Question4_Builder {
    static class Product {
        String a;
        int b;

        Product(String a, int b) {
            this.a = a;
            this.b = b;
        }

        public String toString() {
            return a + ":" + b;
        }
    }

    static class Builder {
        private String a;
        private int b;

        public Builder setA(String a) {
            this.a = a;
            return this;
        }

        public Builder setB(int b) {
            this.b = b;
            return this;
        }

        public Product build() {
            return new Product(a, b);
        }
    }

    public static void main(String[] args) {
        Product p = new Builder().setA("alpha").setB(5).build();
        System.out.println(p);
    }
}
