public class Question12_Command {
    interface Command {
        void execute();
    }

    static class Light {
        void on() {
            System.out.println("Light on");
        }

        void off() {
            System.out.println("Light off");
        }
    }

    static class LightOn implements Command {
        Light light;

        LightOn(Light l) {
            light = l;
        }

        public void execute() {
            light.on();
        }
    }

    static class Remote {
        Command slot;

        void setCommand(Command c) {
            slot = c;
        }

        void press() {
            slot.execute();
        }
    }

    public static void main(String[] args) {
        Light l = new Light();
        Remote r = new Remote();
        r.setCommand(new LightOn(l));
        r.press();
    }
}
