import java.io.*;
import java.util.*;
import java.util.Scanner;

public class LongestLines
{
  public static void main(String[] args)
  {
    File file = new File(args[0]);
    Map<Integer, String> sentences = new HashMap<Integer, String>();
    int numLines;
    Scanner scanner = null;
    try
    {
      scanner = new Scanner(file);
      numLines = scanner.nextInt();
      while(scanner.hasNextLine())
      {
        String sen = scanner.nextLine();
        sentences.put(sen.length(), sen);
      }

      for(int i = 0; i < numLines; ++i)
      {
        int maxLen = Collections.max(sentences.keySet());
        System.out.println(sentences.get(maxLen));
        sentences.remove(maxLen);
      }
    }
    catch(FileNotFoundException ex)
    {
      System.out.println("File not found");
    }
  }
}
