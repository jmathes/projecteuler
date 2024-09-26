// See https://aka.ms/new-console-template for more information


using System.Reflection;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length != 1)
        {
            Console.WriteLine("Usage: euler <command | problem number>");
            return;
        }
        string typeName = "Euler.Problems.P" + args[0] + ".Solution";

        Type? type = Type.GetType(typeName);
        if (type == null)
        {
            Console.WriteLine("No such solution: P" + args[0]);
            return;
        }
        if (type.IsDefined(typeof(util.Solver), true))
        {
            Console.WriteLine("Not a solution: P" + args[0]);
            return;
        }
        MethodInfo? methodInfo = type.GetMethod(
            "Solve",
            BindingFlags.Static | BindingFlags.Public);
        if (methodInfo == null)
        {
            Console.WriteLine("Solution exists but Solve method not defined");
            return;
        }
        string? result = (string?)methodInfo.Invoke(null, null);
        Console.WriteLine("Solution: " + result);
    }
}