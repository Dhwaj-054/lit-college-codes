public class Question6_Bridge {
    interface DrawAPI {
        String drawCircle(int r, int x, int y);
    }

    static class RedCircle implements DrawAPI {
        public String drawCircle(int r, int x, int y) {
            return "Red circle";
        }
    }

    static class Shape {
        DrawAPI api;

        Shape(DrawAPI a) {
            api = a;
        }
    }

    static class Circle extends Shape {
        int r, x, y;

        Circle(int r, int x, int y, DrawAPI a) {
            super(a);
            this.r = r;
            this.x = x;
            this.y = y;
        }

        public String draw() {
            return api.drawCircle(r, x, y);
        }
    }

    public static void main(String[] args) {
        System.out.println(new Circle(5, 10, 10, new RedCircle()).draw());
    }
}
