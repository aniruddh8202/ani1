import java.io.*;
public class JavaApplication3
{
    public static void main(String[] args)throws IOException
    {
        char ch='1';
        int i;
         for(i=97;i<=122;i++)
         {
             if (((int)ch)==i)
         System.out.println("It is a character"+ch);
        else
            System.out.println("it is not a character" +ch);
         }
            
    }
}
