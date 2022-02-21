
import java.util.Scanner;

public class TestCaesar {
    public static void main(String[] args) throws Exception {
        // Jomar A. Nacorda
        CaesarCIpher c = new CaesarCIpher();
        c.setPlaintext("Johny");
        c.setKey(4);
        c.encrypt();

        System.out.println(c.getCiphertext());

        CaesarCIpher c2 = new CaesarCIpher("hello", 4);
        c2.encrypt();
        System.out.println(c2.getCiphertext());

        CaesarCIpher c3 = new CaesarCIpher();
        c3.encrypt("eclipse", 8);
        System.out.println(c3.getCiphertext());

        CaesarCIpher c4 = new CaesarCIpher();
        System.out.println(c4.encryptS("structure", 6));

        c.setCiphertext("Nslrc");
        c.setKey(4);
        System.out.println(c.decrypt());

        CaesarCIpher c5 = new CaesarCIpher();
        Scanner s = new Scanner(System.in);
        System.out.print("Enter Plaintext\t: ");
        String plaintext = s.nextLine();

        System.out.print("Type shift\t: ");
        int key = s.nextInt();
        if (c5.isAlpha(plaintext))
            System.out.println("Ciphertext \t: " + c5.encryptS(plaintext, key));
        else {
            System.err.println("Plaintext must be alphabetic");
            System.exit(0);
        }

        c5.fMaker();
        

    }      

}