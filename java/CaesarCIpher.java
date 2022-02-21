import java.io.File;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Scanner;

public class CaesarCIpher {
    private String plaintext, ciphertext;
    private int key;

    public CaesarCIpher() {
        plaintext = ciphertext = "";
        key = 0;
    }

    public CaesarCIpher(String plaintext, int key) {
        this.plaintext = plaintext.toLowerCase();
        ciphertext = "";
        this.key = key;
    }

    public void setPlaintext(String plaintext) {
        this.plaintext = plaintext.toLowerCase();
    }

    public void encrypt() {
        char ch;
        int alphaValue = 0;
        for (int i = 0; i < plaintext.length(); i++) {
            ch = plaintext.charAt(i);
            alphaValue = ch + (key % 26);
            if (alphaValue > 'z') {
                alphaValue -= 26;
            }
            ciphertext += (char) alphaValue;
        }
    }

    public void encrypt(String Plaintext, int key) {
        int ch;
        for (int i = 0; i < Plaintext.length(); i++) {
            ch = (int) Plaintext.charAt(i) + (key % 26);
            if (ch > 'z') {
                ch -= 26;
            }
            ciphertext = ciphertext + (char) ch;
        }

    }

    public String decrypt() {
        String hold = "";
        int ch;
        for (int i = 0; i < ciphertext.length(); i++) {
            ch = (int) ciphertext.charAt(i) - (key % 26);
            if (ch < 'a') {
                ch += 26;
            }
            hold = hold + (char) ch;
        }
        return hold;
    }

    public String decrypt(String ciphertext, int key) {
        String hold = "";
        int ch;
        for (int i = 0; i < ciphertext.length(); i++) {
            ch = (int) ciphertext.charAt(i) - (key % 26);
            if (ch < 'a') {
                ch += 26;
            }
            hold = hold + (char) ch;
        }
        return hold;
    }

    public String encryptS(String plaintext, int key) {
        int ch;
        for (int i = 0; i < plaintext.length(); i++) {
            ch = plaintext.charAt(i) + (key % 26);
            if (ch > 'z') {
                ch -= 26;
            }
            ciphertext += (char) ch;
        }
        return ciphertext;
    }

    public void setKey(int key) {
        this.key = key;
    }

    public String getPlaintext() {
        return plaintext;
    }

    public String getCiphertext() {
        return ciphertext;
    }

    public int getKey() {
        return key;
    }

    public void setCiphertext(String ciphertext) {
        this.ciphertext = ciphertext;
    }
    public void fMaker(){
    try {
        PrintStream t = new PrintStream(new FileOutputStream("HiddenMessage.txt"));
        t.println(getCiphertext());
        t.close();
        System.out.println("Storing to a file HiddenMessage.txt");

        File file = new File("HiddenMessage.txt");
        Scanner sc = new Scanner(file);

        while (sc.hasNextLine())
            System.out.println("Message \t: " + decrypt(sc.nextLine(), key));
    } catch (Exception e) {
        System.out.println("Error");
    }
}
    public boolean isAlpha(String s) {
    if (s == null) {
        return false;
    }

    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (!(c >= 'A' && c <= 'Z') && !(c >= 'a' && c <= 'z') && c != ' ') {
            return false;
        }
    }
    return true;
    }
    
}