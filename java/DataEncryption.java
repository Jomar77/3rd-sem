public class DataEncryption{
    public static void main(String[] args) {
       DataEncryption de = new DataEncryption();
       int key = 4;
       String plainttext = "hello world";

       String ciphertext = de.encrypt(plainttext, key);
       System.out.println("plaintext: " + plainttext);
       System.out.println("Ciphertext: " + ciphertext);
       System.out.println("plaintext: " + de.decrypt(ciphertext, key));
       System.out.println("plaintext: " + de.decryptNew(ciphertext, key));
       System.out.println("ciphertext: " + de.encryptNew(plainttext, key));
    }
    public String encrypt(String plainText, int key) {
        String ciphertext = "";
        int ch;
        for(int i=0; i<plainText.length(); i++) {
            ch = (int)plainText.charAt(i) + (key%26);
            if (ch > 'z') {
                ch -= 26;
            }
            ciphertext = ciphertext + (char)ch;
        }
        return ciphertext;
    }
    public String decrypt(String cipherText, int key) {
        String hold = "";
        int ch;
        for(int i=0; i<cipherText.length(); i++) {
            ch = (int)cipherText.charAt(i) - (key%26);
            if (ch < 'a') {
                ch += 26;
            }
            hold = hold + (char)ch;
        }
        return hold;
    }

    public String decryptNew(String c, int k) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String hold = "";

        char ch;
        int index;
        for(int i=0; i<c.length(); i++) {
            ch = c.charAt(i);
            index = (alphabet.indexOf(ch) - k) % 26;
            if (index < 0) {
                index += 26;
            }
            hold += alphabet.charAt(index);
        }
        return hold;
    }
    public String encryptNew(String p, int ke) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String ciphertext = "";
        char ch;
        int index;
        for(int i=0; i<p.length(); i++) {
            ch = p.charAt(i);
            index = (alphabet.indexOf(ch) + ke) % 26;
                ciphertext = ciphertext + alphabet.charAt(index);
        }
         return (ciphertext);
        
    }
}