import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class FibonacciTests {
    @Test
    public void shouldReturnZeroForZero() {
        assertEquals(0, Fibonacci.fibonacci(0));
    }

    @Test
    public void shouldReturnOneForOne() {
        assertEquals(1, Fibonacci.fibonacci(1));
    }

    @Test
    public void shouldReturnOneForTwo() {
        assertEquals(1, Fibonacci.fibonacci(2));
    }

    @Test
    public void shouldReturnTwoForThree() {
        assertEquals(2, Fibonacci.fibonacci(3));
    }

    @Test
    public void shouldThrowExceptionForNegativeNumber() {
        assertThrows(IllegalArgumentException.class, () -> Fibonacci.fibonacci(-1));
    }

    @Test
    public void shouldThrowExceptionForBiggerNegativeNumber() {
        assertThrows(IllegalArgumentException.class, () -> Fibonacci.fibonacci(-6));
    }

    @Test
    public void shouldReturnCorrectNumberFor46() {
        assertEquals(1836311903,Fibonacci.fibonacci(46));
    }

    @Test
    public void shouldThrowExceptionForNumberGreaterThan46() {
        assertThrows(IllegalArgumentException.class, () -> Fibonacci.fibonacci(47));
    }



    @Test
    public void shouldReturnFalseForNegativeNumber(){
        assertFalse(Fibonacci.isFibonacci(-1));
    }

    @Test
    public void shouldReturnTrueForZero() {
        assertTrue(Fibonacci.isFibonacci(0));
    }

    @Test
    public void shouldReturnTrueForOne() {
        assertTrue(Fibonacci.isFibonacci(1));
    }

    @Test
    public void shouldReturnTrueForTwo() {
        assertTrue(Fibonacci.isFibonacci(2));
    }

    @Test
    public void shouldReturnFalseForFour() {
        assertFalse(Fibonacci.isFibonacci(4));
    }

    @Test
    public void shouldReturnTrueFor1836311903() {
        assertTrue(Fibonacci.isFibonacci(1836311903));
    }


    @Test
    public void shouldReturnFibonacciSequence() {
        int[] expected = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34};
        assertArrayEquals(expected, Fibonacci.fibonacciSequence(10));
    }

    @Test
    public void shouldReturnEmptyArrayForZero() {
        int[] expected = {};
        assertArrayEquals(expected, Fibonacci.fibonacciSequence(0));
    }

    @Test
    public void shouldReturnArrayWithOneElementForOne() {
        int[] expected = {0};
        assertArrayEquals(expected, Fibonacci.fibonacciSequence(1));
    }

    @Test
    public void shouldThrowExceptionForNegativeSequenceLength() {
        assertThrows(IllegalArgumentException.class, () -> Fibonacci.fibonacciSequence(-1));
    }

    @Test
    public void shouldReturnFibonacciSequenceFor47Numbers(){
        int[] expected = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
                4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
                1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
                102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903};
        int[] result = Fibonacci.fibonacciSequence(47);

        assertArrayEquals(expected, result);
    }

}