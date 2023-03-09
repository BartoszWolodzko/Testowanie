import org.jetbrains.annotations.NotNull;

public class Fibonacci {
    public static int fibonacci(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be >= 0");
        }
        if (n > 46) {
            throw new IllegalArgumentException("n must be <= 46");
        }
        int f0 = 0;
        int f1 = 1;
        for (int i = 0; i < n; i++) {
            int f2 = f0 + f1;
            f0 = f1;
            f1 = f2;
        }
        return f0;
    }

    public static boolean isFibonacci(int n) {
        if (n < 0) {
            return false;
        }
        if (n == 0) {
            return true;
        }
        int a = 0;
        int b = 1;
        while (b < n) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b == n;
    }

    public static int @NotNull [] fibonacciSequence(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be >= 0");
        }
        if (n > 47) {
            throw new IllegalArgumentException("n must be <= 47");
        }
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = fibonacci(i);
        }
        return result;
    }
}