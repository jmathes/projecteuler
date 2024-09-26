namespace Euler.Problems.P1
{
    public class Solution : ISolution
    {
        public static string Solve()
        {
            /// <summary>
            /// https://projecteuler.net/problem=1
            ///
            /// Multiples of 3 or 5
            ///
            /// If we list all the natural numbers below 10 that are
            /// multiples of 3 or 5, we get 3, 5, 6, and 8, summing to 23.
            /// Find the sum of all the multiples of 3 or 5 below 1000.
            /// </summary>
            /// <remarks>
            /// Basically, this is fizzbuzz
            /// </remarks>
            int sum = 0;
            for (int i = 0; i < 1000; i++)
            {
                if (i % 3 == 0 || i % 5 == 0)
                {
                    sum += i;
                }
            }
            return sum.ToString();
        }
    }
}