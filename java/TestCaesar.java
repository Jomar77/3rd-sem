import java.io.File;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Scanner;

public class TestCaesar {
    public static void main(String[] args) throws Exception {
        // Jomar A. Nacorda
        CaesarCIpher c = new CaesarCIpher();
        c.setPlaintext("hello world");
        c.setKey(4);
        c.encrypt();

        System.out.println("plaintext: " + c.getPlaintext());

        CaesarCIpher c2 = new CaesarCIpher("hello world", 4);
        c2.encrypt();
        System.out.println("Ciphertext: " + c2.getCiphertext());

        CaesarCIpher c3 = new CaesarCIpher();
        c3.encrypt("eclipse", 8);
        System.out.println( c3.getCiphertext());

        CaesarCIpher c4 = new CaesarCIpher();
        System.out.println(c4.encryptS("structure", 6));

        c.setCiphertext("nslrc");
        c.setKey(4);
        System.out.println(c.decrypt());

        CaesarCIpher c5 = new CaesarCIpher();
        Scanner s = new Scanner(System.in);
        System.out.print("Enter Plaintext\t: ");
        String plaintext = s.nextLine();

        System.out.print("Type shift\t: ");
        int key = s.nextInt();
        if(isAlpha(plaintext))
            System.out.println("Ciphertext \t: " + c5.encryptS(plaintext, key));
        else{
            System.err.println("Plaintext must be alphabetic");
            System.exit(0);
        }


    try{
        PrintStream t = new PrintStream(new FileOutputStream("HiddenMessage.txt"));
        t.println(c5.getCiphertext());
        t.close();
        System.out.println("Storing to a file HiddenMessage.txt");

        File file = new File("HiddenMessage.txt");
        Scanner sc = new Scanner(file);

        while (sc.hasNextLine())
            System.out.println("Message \t: " +c5.decrypt(sc.nextLine(), key));
    }
    catch(Exception e){
        System.out.println("Error");
    }
    }


    public static boolean isAlpha(String s) {
        if (s == null) {
            return false;
        }

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if (!(c >= 'A' && c <= 'Z') && !(c >= 'a' && c <= 'z') && c!= ' ') {
                return false;
            }
        }
        return true;
    }

}
