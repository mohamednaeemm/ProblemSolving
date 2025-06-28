public class Solution {
    public static void main(String[] args) {
        int n = 123;
        int finalResult = subtractProductAndSum(n);
        System.out.println("Result of subtracting product and sum: " + finalResult);
    }

    public static int subtractProductAndSum(int n) {
        int sum = 0;
        int product = 1;
        while (n > 0) {
            int digit = n % 10;
            sum += digit; // Add the last digit to the sum
            product *= digit;
            n /= 10; // Remove the last digit from the number
        }
        return product - sum;
    }
}


