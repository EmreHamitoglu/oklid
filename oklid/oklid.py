using System;

class Program
{
    static int FirstFactorial(int num)
    {
        if (num == 0 || num == 1)
            return 1;
        else
            return num * FirstFactorial(num - 1);
    }

    static void Main(string[] args)
    {
        // Test the function with example inputs
        Console.WriteLine(FirstFactorial(4)); // Output: 24
        Console.WriteLine(FirstFactorial(8)); // Output: 40320
    }
}