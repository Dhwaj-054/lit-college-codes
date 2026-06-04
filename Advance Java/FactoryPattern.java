public class Question1_FactoryPattern {
    interface Shape {
        String draw();
    }

    static class Circle implements Shape {
        public String draw() {
            return "Circle drawn";
        }
    }

    static class Square implements Shape {
        public String draw() {
            return "Square drawn";
        }
    }

    static class ShapeFactory {
        public static Shape create(String type) {
            if ("circle".equalsIgnoreCase(type))
                return new Circle();
            return new Square();
        }
    }

    public static void main(String[] args) {
        System.out.println(ShapeFactory.create("circle").draw());
    }
}
