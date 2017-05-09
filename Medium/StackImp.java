import java.io.*;
import java.util.*;
import java.util.Scanner;
import java.util.Stack;

public class StackImp
{
  public static void main(String[] args)
  {
    File in = new File(args[0]);
    Scanner scanner = null;
    try
    {
      scanner = new Scanner(in);
      Deque<Integer> stack;

      //Read all the line
      while(scanner.hasNextLine())
      {
        stack = new ArrayDeque<Integer>();
        String line = scanner.nextLine();
        Scanner s = new Scanner(line);

        while(s.hasNextInt())
        {
          stack.push(s.nextInt());
        }

        while(stack.size() > 0)
        {
          System.out.print(stack.pop() + " " );
          if(stack.size() > 0)
          {
            stack.pop();
          }
        }
        System.out.println();
      }
    }
    catch(FileNotFoundException ex)
    {
      System.out.println("Could not find the file");
    }
  }
}
