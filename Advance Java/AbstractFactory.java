public class Question2_AbstractFactory {
    interface Button {
        String paint();
    }

    static class WinButton implements Button {
        public String paint() {
            return "Windows Button";
        }
    }

    static class MacButton implements Button {
        public String paint() {
            return "Mac Button";
        }
    }

    interface GUIFactory {
        Button createButton();
    }

    static class WinFactory implements GUIFactory {
        public Button createButton() {
            return new WinButton();
        }
    }

    static class MacFactory implements GUIFactory {
        public Button createButton() {
            return new MacButton();
        }
    }

    public static void main(String[] args) {
        GUIFactory f = new WinFactory();
        System.out.println(f.createButton().paint());
    }
}
