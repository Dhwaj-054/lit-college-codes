import java.util.ArrayDeque;
import java.util.Deque;

public class Question13_Interpreter {
    static class Interpreter {
        static int interpret(String expr) {
            Deque<Integer> st = new ArrayDeque<>();
            String[] parts = expr.split("\\s+");
            for (String p : parts) {
                if (p.matches("-?\\d+")) {
                    st.push(Integer.parseInt(p));
                } else {
                    int b = st.pop();
                    int a = st.pop();
                    switch (p) {
                        case "+":
                            st.push(a + b);
                            break;
                        case "-":
                            st.push(a - b);
                            break;
                        case "*":
                            st.push(a * b);
                            break;
                        case "/":
                            st.push(a / b);
                            break;
                    }
                }
            }
            return st.pop();
        }
    }

    public static void main(String[] args) {
        System.out.println(Interpreter.interpret("5 3 + 2 *"));
    }
}
